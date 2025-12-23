import random


def main() -> None:
    target = random.randint(1, 100)
    attempts = 0

    print("Guess the number between 1 and 100!")
    while True:
        guess_input = input("Enter your guess: ")
        try:
            guess = int(guess_input)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break


if __name__ == "__main__":
    main()
