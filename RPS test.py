from random import randint

Your_score = 0
Bot_score = 0

while True:
    COM_CHOICE = randint(1, 3)
    print()
    print("Please turn caps locks on for this game")
    USER_CHOICE = input("Choose R (Rock), P (Paper), S (Scissors)   : ")

    # COM CHOICE
    if COM_CHOICE == 1:
        RPS = "R"
        print("BOT: ROCK")
    elif COM_CHOICE == 2:
        RPS = "P"
        print("BOT: PAPER")
    elif COM_CHOICE == 3:
        RPS = "S"
        print("BOT: SCISSORS")

    if RPS == "R" and USER_CHOICE == "R":
        print("Tie!")

    if RPS == "P" and USER_CHOICE == "R":
        Bot_score += 1
        print("You lose!")

    if RPS == "S" and USER_CHOICE == "R":
        Your_score += 1
        print("You win!")

    if RPS == "R" and USER_CHOICE == "P":
        Your_score += 1
        print("You win!")

    if RPS == "P" and USER_CHOICE == "P":
        print("Tie!")

    if RPS == "S" and USER_CHOICE == "P":
        Bot_score += 1
        print("You lose!")

    if RPS == "R" and USER_CHOICE == "S":
        Bot_score += 1
        print("You lose!")

    if RPS == "P" and USER_CHOICE == "S":
        Your_score += 1
        print("You win!")

    if RPS == "S" and USER_CHOICE == "S":
        print("Tie!")

    print(f"Your score: {Your_score}")
    print(f"Bot score: {Bot_score}")

