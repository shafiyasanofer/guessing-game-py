import random

def play_game():
    name = input("Enter your name: ")
    # increased random number generation to make the game harder
    number_to_guess = random.randint(1, 1000)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

    # Save to scoreboard
    with open("scoreboard.txt", "a") as file:
        file.write(f"{name} - {attempts} attempts\n")

    print("Score saved to scoreboard.txt")

play_game()
