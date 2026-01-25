from models import Board

import time
import os
import sys
import select
import tty
import termios


# Check if there is any input in the keyboard without blocking the program
def is_data():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def main():
    board = Board()
    running = True

    old_settings = termios.tcgetattr(sys.stdin) # Save original terminal settings

    try:
        tty.setcbreak(sys.stdin.fileno()) # RAW mode: instant reading

        os.system("clear")

        while running:
            if not board.insert_piece():
                running = False
                continue
            
            print("\033[H" + board.render()) # Move cursor to the start (like os.system("clear") but avoiding flickering)

            bottom = False
            last_fall = time.time()

            # Main loop
            while not bottom:
                current_time = time.time()
                
                # --- Gravity logic ---
                if current_time - last_fall > 1:
                    if not board.move_piece_down():
                        print("\033[H" + board.render(block_piece=True))
                        bottom = True # Piece in board's bottom
                    else:
                        print("\033[H" + board.render())
                    
                    last_fall = time.time() # Reset timer

                # --- Listen keyboard (without blocking) ---
                if is_data():
                    key = sys.stdin.read(1).lower() # Read 1 char

                    # Detect escape sequence for arrows
                    if key == "\x1b": # If it's the start of an escape sequence
                        # Read the next 2 chars: "[" and direction
                        seq = sys.stdin.read(2)
                        key = seq[1] # This is "A", "B", "C" or "D"
                    
                    moved = False
                    
                    if key == "D": # Move left
                        board.move_piece_horizontally("left")
                        moved = True
                    elif key == "C": # Move right
                        board.move_piece_horizontally("right")
                        moved = True
                    elif key == "A": # Rotate right
                        board.rotate_piece("right")
                        moved = True
                    elif key == "z": # Rotate left
                        board.rotate_piece("left")
                        moved = True
                    elif key == "B": # Fall fast
                        if board.move_piece_down():
                            last_fall = time.time()
                            moved = True
                        else:
                            bottom = True
                    elif key == "q": # End game
                        running = False
                        break
                    
                    if moved:
                        print("\033[H" + board.render())
                
                if bottom:
                    break

                # Little stop to not saturate the CPU
                time.sleep(0.05)

            # Fix piece in the board
            if running: # Only if we don't end game with q
                print("\033[H" + board.render(block_piece=True))
                board.remover()
    
    finally:
        # --- IMPORTANT: Restore original configuration no matter what happens ---
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        os.system("clear")
        print("Juego terminado.")
    
            
if __name__ == "__main__":
    main()