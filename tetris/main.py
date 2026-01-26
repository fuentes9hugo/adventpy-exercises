from models import Game

import time
import os
import sys
import select
import tty
import termios


def main():
    game = Game()
    game.run()
    
            
if __name__ == "__main__":
    main()