import random


# Some colours to choose from...

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


score = 10

print("Welcome to the 'Number-guessing-game'.")
print("To stop anytime...enter 'q'")
rnd_num = random.randint(0, 10)
print("Spoiler:", rnd_num)
while True:
    g = input(f"{bcolors.ENDC}Guess the number between 0-10: {bcolors.ENDC}")
    if g == 'q':
        print("Bye, bye.")
        break
    myvar = int(g)
    if myvar is rnd_num:
        print('Congrats')
        score += 10
        print(f'{bcolors.WARNING}Score:{bcolors.WARNING}', score)
        rnd_num = random.randint(0, 10)
        print(f"{bcolors.ENDC}Spoiler:{bcolors.ENDC}", rnd_num)
    else:
        score -= 10
        print('No\n')
        print(f"{bcolors.OKBLUE}Score:{bcolors.OKBLUE}", score)
        print(f"{bcolors.ENDC}Spoiler:{bcolors.ENDC}", rnd_num)