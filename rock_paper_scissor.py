import random

chances = 5  # Set the number of chances

while chances > 0:
    user = int(input("Enter your number between 0 to 2 (0 for rock, 1 for paper, and 2 for scissors): "))
    l = [0, 1, 2]
    if user > 2:
        print("Given number is not valid")
    else:
        r = random.choice(l)
        print("Computer's choice:", r)
        if user == r:
            print("It's a draw")
        elif (user == 0 and r == 2) or (user == 2 and r == 1):
            print("You won")
        elif r > user:
            print("Computer won")
        elif user > r:
            print("You won")
    
    chances -= 1

    if chances > 0:
        play_again = input("Press 'y' to play another round or any other key to exit: ")
        if play_again.lower() != 'y':
            break

print("Thanks for playing!")
