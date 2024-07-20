import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    computer_score = 0
    rounds = 0
    
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Instructions:")
    print("1. Choose either 'rock', 'paper', or 'scissors'.")
    print("2. The computer will also make a choice.")
    print("3. Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
    print("4. First to reach 5 wins is the champion!")
    
    while user_score < 5 and computer_score < 5:
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        
        rounds += 1
        display_result(user_choice, computer_choice, winner)
        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        if user_score == 5 or computer_score == 5:
            break
        
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    if user_score > computer_score:
        print("\nCongratulations! You are the champion!")
    else:
        print("\nBetter luck next time! The computer is the champion!")
    print(f"Total rounds played: {rounds}")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
