import random

user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors Game!")
print("Instructions:")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'exit' to quit the game.\n")

while True:
    user_choice = input("Your choice (rock/paper/scissors): ").lower()

    if user_choice == "exit":
        print("\nFinal score:")
        print(f"You: {user_score} || Computer: {computer_score}")
        print("Thanks for playing the game!")
        break  

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please choose rock, paper, or scissors.\n")
        continue  

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif ((user_choice == "rock" and computer_choice == "scissors") or
          (user_choice == "scissors" and computer_choice == "paper") or
          (user_choice == "paper" and computer_choice == "rock")):
        result = "You win!! :)"
        user_score += 1
    else:
        result = "You lose! :("
        computer_score += 1

    print(result)
    print(f"Score -> You: {user_score} || Computer: {computer_score}\n")
