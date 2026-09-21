from colorama import Fore
from utils.audio_manager import AudioManager



audio = AudioManager()

class Player:
    colors = {
        1: Fore.BLUE,
        2: Fore.RED,
        3: Fore.YELLOW,
        4: Fore.MAGENTA
    }

    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.color = self.colors.get(number)
        self.position = 0

    def move(self, blocks_to_move, num_of_blocks):
        """Make a player move on the board for an amount given"""
        audio.play(2)
        self.position += blocks_to_move

        if self.position > num_of_blocks:
            go_back = self.position - num_of_blocks
            self.position -= go_back * 2
