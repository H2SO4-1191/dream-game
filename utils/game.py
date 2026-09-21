from colorama import Fore
from utils.player import Player
from utils.dice import Dice
from utils.audio_manager import AudioManager
import time


audio = AudioManager()

class Game:
    def __init__(self, num_of_players, num_of_dice, num_of_blocks):
        """Check game rules first and setting the board only if everything is intact"""
        if num_of_players < 1 or num_of_players > 4:
            raise ValueError(Fore.RED + "Number of players must be between 1 and 4." + Fore.RESET)
        
        if num_of_dice < 1:
            raise ValueError(Fore.RED + "Number of dices must at least be 1." + Fore.RESET)
        
        if num_of_dice*6 > num_of_blocks:
            raise ValueError(Fore.RED + f"Number of blocks must be more than the maximum dice result in total. "
                                        f"Right now number of dice is {num_of_dice} so number of blocks must be over the number"
                                        f"of dice multiplied by 6. Pick a number over {num_of_dice*6}." + Fore.RESET)
        
        self.num_of_dice = num_of_dice
        self.num_of_players = num_of_players
        self.num_of_blocks = num_of_blocks

        self.players = []
        self.dices = []
        self.timer = 0
        self.start_time = None

    def setup_board(self):
        """Setup the board game based on the number of players and dice"""
        for i in range(self.num_of_players):
            name = input(Fore.GREEN + f"Enter a name for player {i+1}: " + Fore.RESET)
            audio.play(5)
            player = Player(i+1, name)
            self.players.append(player)
        
        for i in range(self.num_of_dice):
            dice = Dice(i+1)
            self.dices.append(dice)

        self.timer = int(input(Fore.GREEN + "Enter game time in minutes (0 = off): " + Fore.RESET))
        audio.play(5)
        while self.timer < 0:
            self.timer = int(input("Enter a valid time (>= 0): "))
            audio.play(5)

        if self.timer > 0:
            self.start_time = time.time()
                
    def state(self):
        """Return the state of the game after each round with all players and their positions
           ordered based on their distance to the end"""
        for i in range(len(self.players)):
            swapped = False
            for j in range(0, len(self.players) - i - 1):
                if(self.players[j].position < self.players[j+1].position):
                    self.players[j], self.players[j + 1] = self.players[j + 1], self.players[j]
                    swapped = True
            if not swapped: 
                break

        state_line = ""
        for i in range(len(self.players)):
            state_line += self.players[i].color + f"| {self.players[i].name} - {self.players[i].position} |" + Fore.RESET

        if self.timer > 0:
            elapsed = int(time.time() - self.start_time)
            remaining = max(0, self.timer * 60 - elapsed)
            minutes = remaining // 60
            seconds = remaining % 60
            state_line += f" | Remaining Time = {minutes:02d}:{seconds:02d}"

        print(state_line + Fore.RESET)

    def check_game_over(self, player):
        """Check if the game had reach an ending state by the end of each turn"""
        if player.position == self.num_of_blocks:
            print(Fore.GREEN + f"Game Over. {player.color}{player.name}{Fore.GREEN} is the winner!" + Fore.RESET)
            return self.game_over()

        if self.timer > 0:
            elapsed = int(time.time() - self.start_time)
            remaining = max(0, self.timer * 60 - elapsed)
            if remaining <= 0:
                print(Fore.GREEN + "Time is up. Player closest to the end is the winner!" + Fore.RESET)
                return self.game_over()

        return None

    def game_over(self):
        """Make the user take a choice upon ending a game"""
        audio.play(4)

        choice = input(
            Fore.GREEN +
            "Do you wish to play again?\n"
            + Fore.RESET +
            "1- Rematch with same setup.\n"
            "2- New setup.\n"
            "3- Exit to main menu.\n"
            + Fore.GREEN + "Enter 1, 2 or 3: " + Fore.RESET
        )
        audio.play(5)

        while choice not in ["1", "2", "3"]:
            choice = input(Fore.GREEN + "Enter 1, 2 or 3: " + Fore.RESET)
            audio.play(5)

        return choice
