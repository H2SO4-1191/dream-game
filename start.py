from utils.game import Game
from utils.audio_manager import AudioManager
from colorama import Fore



num_of_players = 0
num_of_dice = 0
num_of_blocks = 0
game = None
audio = AudioManager()

def main():
    audio.play_music()

    while True:
        print(Fore.GREEN + "Welcome to the game that I had seen in my dream. Wish to play it? (Ctrl + C to exit at any time)" + Fore.RESET)

        choice = input("1- Play.\n2- Rules.\n3- Exit\n" + Fore.GREEN + "Enter 1, 2 or 3: " + Fore.RESET)
        audio.play(5)
        while choice not in ["1", "2", "3"]:
            choice = input(Fore.GREEN + "Enter 1, 2 or 3: " + Fore.RESET)
            audio.play(5)

        if choice == "1":
            take_rules()
            game = Game(num_of_players, num_of_dice, num_of_blocks)
            game.setup_board()
            play(game)
        elif choice == "2":
            show_rules()
        else:
            exit()

def show_rules():
    print(Fore.GREEN + """
╔══════════════════════════════════════════════════════╗
║                     GAME RULES                       ║
╚══════════════════════════════════════════════════════╝
""" + Fore.RESET)
    print("""  The dream game is a turn-based race to the finish line.

  OBJECTIVE:
    Be the first player to land exactly on the last block
    to win the game. If time runs out, the player closest
    to the end wins.

  SETUP:
    - 1 to 4 players can compete.
    - Choose how many dice to roll each turn (at least 1).
    - Choose the number of blocks on the board. It must be
      greater than the maximum possible dice roll total
      (dice count × 6).
    - Optionally set a time limit in minutes. Set to 0 to
      play without a timer.

  GAMEPLAY:
    - Players take turns in order. On your turn, press
      Enter to roll all dice.
    - Your piece moves forward by the total of all dice.
    - If you would overshoot the last block, you bounce
      back by the excess amount.
    - If you land on the same block as another player,
      that player is sent back to the start!

  WINNING:
    - Land exactly on the final block → instant win.
    - Time runs out → the player furthest ahead wins.

  After each game, you can rematch, start fresh, or
  return to the main menu.
""")
    input(Fore.GREEN + "Press Enter to go back..." + Fore.RESET)

def take_rules():
    global num_of_players, num_of_dice, num_of_blocks

    print("Enter the rules by which you would like to play...")

    num_of_players = 0
    while num_of_players < 1 or num_of_players > 4:
        try:
            num_of_players = int(input(Fore.GREEN + "Enter the number of players (1-4): " + Fore.RESET))
            audio.play(5)
            if num_of_players < 1 or num_of_players > 4:
                print(Fore.RED + "Number of players must be between 1 and 4." + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Fore.RESET)

    num_of_dice = 0
    while num_of_dice < 1:
        try:
            num_of_dice = int(input(Fore.GREEN + "Enter the number of dice: " + Fore.RESET))
            audio.play(5)
            if num_of_dice < 1:
                print(Fore.RED + "Must have at least 1 dice." + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Fore.RESET)

    num_of_blocks = 0
    while num_of_blocks <= num_of_dice * 6:
        try:
            num_of_blocks = int(input(Fore.GREEN + f"Enter the number of blocks (must be over {num_of_dice * 6}): " + Fore.RESET))
            audio.play(5)
            if num_of_blocks <= num_of_dice * 6:
                print(Fore.RED + f"Number of blocks must be greater than {num_of_dice * 6}." + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Fore.RESET)

def play(game):
    playing = True
    turn = 0

    while playing:
        if turn >= game.num_of_players:
            turn = 0

        player = game.players[turn]
        input(player.color + f"{player.name}, Press Enter to roll dice..." + Fore.RESET)

        blocks_to_move = 0
        for i in range(game.num_of_dice):
            dice = game.dices[i]
            dice.roll()
            blocks_to_move += dice.result
        print(f"{player.name} will move {blocks_to_move} blocks!")

        player.move(blocks_to_move, game.num_of_blocks)

        for other in game.players:
            if other is not player and other.position == player.position:
                other.position = 0
                audio.play(3)
                print(other.color + f"{other.name} got sent back to start!" + Fore.RESET)

        game.state()

        result = game.check_game_over(player)
        if result == "1":
            # Rematch with same setup — reset positions and restart
            for p in game.players:
                p.position = 0
            import time
            if game.timer > 0:
                game.start_time = time.time()
            turn = 0
        elif result == "2":
            # New setup — break out to main loop
            playing = False
        elif result == "3":
            # Exit to main menu — break out to main loop
            playing = False

        turn += 1

if __name__ == "__main__":
    main()
