import random
import sys
from colorama import Fore, Back, init
init(autoreset=True)

def print_menu():
    print("\n\n\n")
    print(Fore.BLUE + "{}" * 30)
    print(Fore.LIGHTYELLOW_EX + '''
                                   ,--.,--.        
       ,--.   ,--. ,---. ,--.--. ,-|  ||  | ,---.  
       |  |.'.|  || .-. ||  .--'' .-. ||  || .-. : 
       |   .'.   |' '-' '|  |   \ `-' ||  |\   --. 
       '--'   '--' `---' `--'    `---' `--' `----'                                                                                                                                                                
    ''')
    print(Fore.BLUE + "{}" * 30)
    print("\n")
    print("  Enter a five letter word. You get 6 guesses.\n\n")

def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)


# word = read_random_word()
play_again = ""

while play_again != "n":
    print_menu()
    word = read_random_word()
    for attempt in range(1, 7):
        guess = input("  Enter your word:   ").lower()
        print()
        # sys.stdout.write('\x1b[1A')
        # sys.stdout.write('\x1b[2K')

        for i in range( min(len(guess), 5)):
            if guess[i] == word[i]:
                print(Back.GREEN + guess[i], end="")
            elif guess[i] in word:
                print(Back.LIGHTYELLOW_EX + guess[i], end="")
            else:
                print(guess[i], end="")
        print("\n   ")
        print(Fore.BLUE + "{}" * 30)
        print("\n   ")

        if guess == word:
            print(Fore.LIGHTGREEN_EX + "\n  You guessed the word in", attempt, Fore.LIGHTGREEN_EX + "tries!")
            break

        elif attempt == 6:
            print(Fore.RED + "\n  You ran out of guesses! The word was", word, Fore.RED + ". Better luck next time...")

    play_again = input(Fore.LIGHTYELLOW_EX + "\n  Enter 'n' to exit or enter any other key to play again. ")
    if play_again == "n":
        print(Fore.LIGHTGREEN_EX + "\n\n  Thanks for playing!\n\n\n\n\n")
        break