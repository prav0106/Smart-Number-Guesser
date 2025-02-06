import random

def number_guessing_game():
    levels = {"Easy": 50, "Medium": 100, "Hard": 200}
    print("Select Difficulty: Easy, Medium, Hard")
    difficulty = input("Enter difficulty level: ").capitalize()
    max_num = levels.get(difficulty, 100)  # Default to Medium if input is invalid
    
    number = random.randint(1, max_num)
    attempts = 0
    print(f"Guess a number between 1 and {max_num}")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess > number:
                print("Lower number please")
            elif guess < number:
                print("Higher number please")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    number_guessing_game()
