import random, sys, time
from colorama import Fore
from utils.audio_manager import AudioManager


audio = AudioManager()

class Dice:
    def __init__(self, number):
        self.number = number
        self.result = None

    def roll(self):
        """Roll a dice with CLI animation"""
        audio.play(1)

        for i in range(15):
            temp = random.randint(1, 6)
            sys.stdout.write(f"\rRolling{'.' * (i % 4)} {temp}")
            sys.stdout.flush()
            time.sleep(0.08)

        self.result = random.randint(1, 6)

        sys.stdout.write(Fore.GREEN + f"\rResult: {self.result}   \n" + Fore.RESET)
