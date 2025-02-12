# Pavettra_python_game
import random

# List of phrases for the game
phrases = [
    "PYTHON PROGRAMMING",
    "HELLO WORLD",
    "MACHINE LEARNING",
    "ARTIFICIAL INTELLIGENCE",
    "SOFTWARE ENGINEERING"
]

# Wheel values
wheel_values = [100, 200, 300, 400, 500, "BANKRUPT", "LOSE A TURN"]

def spin_wheel():
    return random.choice(wheel_values)

def display_puzzle(puzzle, guessed_letters):
    displayed = ""
    for letter in puzzle:
        if letter in guessed_letters or letter == " ":
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()

def play_game():
    puzzle = random.choice(phrases)
    guessed_letters = set()
    player_score = 0
    
    print("Welcome to Wheel of Fortune!")
    
    while True:
        print("\nPuzzle: ", display_puzzle(puzzle, guessed_letters))
        print("Options: 1. Spin the wheel 2. Guess a letter 3. Quit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == "3":
            print("Thanks for playing! Goodbye.")
            break
        
        if choice == "1":
            spin_result = spin_wheel()
            
            if spin_result == "BANKRUPT":
                print("Oh no! You went BANKRUPT!")
                player_score = 0
            elif spin_result == "LOSE A TURN":
                print("You lost your turn!")
            else:
                print(f"Your score  {spin_result} points!")
                guess = input("Guess a letter: ").upper()
                
                if guess in guessed_letters:
                    print("You've already guessed that letter!")
                    continue
                
                guessed_letters.add(guess)
                
                if guess in puzzle:
                    print(f"Good job! The letter {guess} is in the puzzle!")
                    player_score += spin_result
                else:
                    print(f"Sorry! The letter {guess} is not in the puzzle.")
        elif choice == "2":
            solve = input("Do you want to solve the puzzle? (yes/no): ").lower()
            if solve == "yes":
                solution = input("Enter your solution: ").upper()
                if solution == puzzle:
                    print(f"Congratulations! You solved the puzzle! Your final score: {player_score}")
                    break
                else:
                    print("Wrong solution! Try again.")
        
        print(f"Your current score: {player_score}")

if __name__ == "__main__":
    play_game()
