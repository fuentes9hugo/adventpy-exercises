from .board import Board

import time
import os
import sys
import select
import tty
import termios
import pickle
from pathlib import Path


class Game:
    def __init__(self) -> None:
        self._board: Board = Board()
        self._running: bool = True

        self._old_settings = termios.tcgetattr(sys.stdin)  # Save original terminal settings

        self._game_modes: dict[str, float] = {"Easy": 1, "Medium": 0.5, "Hard": 0.2}

        self._fall_speed: float = tuple(self._game_modes.values())[self._game_mode_selector()]
        self._last_fall: float = time.time() # Reset timer
        
        self._solidify: bool = False
        
        self._score: int = 0

    
    # Set terminal config
    def _setup_terminal(self) -> None:
        tty.setcbreak(sys.stdin.fileno())  # RAW mode: instant reading
        os.system("clear")

    
    # --- IMPORTANT: Restore original configuration no matter what happens ---
    def _restore_terminal(self) -> None:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self._old_settings)
        os.system("clear")


    # Check if there is any input in the keyboard without blocking the program
    def _is_data(self):
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
    

    def _game_mode_selector(self):
        os.system("clear")
        print("<--- TETRIS --->\n")
        print("Z -> rotate left | ARROW UP -> rotate right\n")
        print("ARROW LEFT -> move left | ARROW RIGHT -> move right\n")
        print("Q -> exit")
        time.sleep(2)
        difficulty = 0
        while difficulty not in ("1", "2", "3"):
            os.system("clear")
            for i, mode in enumerate(self._game_modes.items(), start=1):
                print(f"{i}- {mode[0]}: {mode[1]}s")
            
            difficulty = input("Choose difficulty (piece's fall delay): ")

        return int(difficulty) - 1
    
    
    # Save score in a pickle file and show ranking
    def _save_score(self):
        print("--- GAME OVER ---")
        time.sleep(1)
        os.system("clear")
        name = input("Your name: ")
        os.system("clear")
        print("--- RANKING ---")
        
        # Find absolute path
        BASE_DIR = Path(__file__).resolve().parent.parent
        file_path = BASE_DIR / "score" / "score.pkl"

        try:
            with open(file_path, "rb") as score_file:
                score = pickle.load(score_file)
                if not name in score:
                    score[name] = self._score

                else:
                    if score[name] < self._score: score[name] = self._score
            
            with open(file_path, "wb") as score_file:
                pickle.dump(score, score_file)
            
            for i, person in enumerate(sorted(score.items(), key=lambda x: x[1], reverse=True)[:3], start=1):
                print(f"{i}- {person[0]}: {person[1]} points")
                
        except FileNotFoundError:
            score = {name: self._score}
            with open(file_path, "wb") as score_file:
                pickle.dump(score, score_file)
            
            
            print(f"1- {name}: {self._score} points")


    # --- Listen keyboard (without blocking) ---
    def _handle_input(self) -> bool:
        if not self._is_data():
            return False

        key = sys.stdin.read(1).lower()  # Read 1 char

        # Detect escape sequence for arrows
        if key == "\x1b": # If it's the start of an escape sequence
            # Read the next 2 chars: "[" and direction
            seq = sys.stdin.read(2)
            key = seq[1] # This is "A", "B", "C" or "D"
        
        moved = False
        if key == "D": # Move left
            self._board.move_piece_horizontally("left")
            moved = True
        elif key == "C": # Move right
            self._board.move_piece_horizontally("right")
            moved = True
        elif key == "A": # Rotate right
            self._board.rotate_piece("right")
            moved = True
        elif key == "z": # Rotate left
            self._board.rotate_piece("left")
            moved = True
        elif key == "B": # Fall fast
            if self._board.move_piece_down():
                self._last_fall = time.time()
                moved = True
        elif key == "q": # End game
            self._running = False
            
        return moved


    # --- Gravity logic ---
    def _update(self) -> bool:
        current_time = time.time()
        if current_time - self._last_fall >= self._fall_speed: # Delta time
            if not self._board.move_piece_down():
                # Piece in board's bottom
                self._solidify = True

            self._last_fall = current_time
            return True
        
        return False
    

    # Display board and score
    def _render(self) -> None:
        print("\033[2J\033[H" + self._board.render(self._solidify)) # Clear screen and move cursor to the start

        print(f"Score: {self._score}")
        print("Q -> exit")

        if self._solidify:
            self._score += self._board.remover()


    # Game loop
    def run(self) -> None:
        self._setup_terminal()
        try:
            # New piece loop
            while self._running:
                if not self._board.insert_piece():
                    self._running = False

                self._solidify = False
                self._last_fall = time.time()
                
                if self._running: self._render()

                # Main loop
                while not self._solidify and self._running:
                    input_moved = self._handle_input()
                    gravity_moved = self._update()

                    if input_moved or gravity_moved:
                        self._render()

                    time.sleep(0.05) # Little stop to not saturate the CPU
        finally:
            self._restore_terminal()
            self._save_score()