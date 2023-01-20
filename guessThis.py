# Friday night fun time - we are going to code a little number guesser 

# Import modules 
import random

# Keep track of the number of user's guesses
guessCount = 0

# Ask user for their number
userNumber = input("Hey, what's up. Type your number now, please.\n")

# Check if user provided a digit
while True:

    if userNumber.isdigit(): 
        # Convert user's input to int
        userNumber = int(userNumber)
        break

    # Tell user to provide a valid number
    else: 
        print("Please provide a valid number.")
        userNumber = input()


# Pick a random number between 1 and 100
randomInt = random.randint(0, userNumber)


# Run a loop until the user finds the randomly generated number, then break
while True: 

    # Ask user to guess a number between 0 and the number they provided 
    userGuess = input(f"Guess the number between 0 and {userNumber}.\n")

    # Increase the guess count by 1
    guessCount += 1
    
    # Check if user provided a digit
    if userGuess.isdigit(): 

        # Convert user's input to int
        userGuess = int(userGuess)

    # Tell user to provide a valid number
    else: 
        print("Please provide a valid number.")
        continue

    # If number is correct tell user they were successful
    if userGuess == randomInt:
        print("You got it! Well done!")
        break
    elif userGuess > randomInt:
        print("Try lower!")
    else:
        print("Try higher!")


# Tell users how many times it took them to guess correctly
print(f"It took you {guessCount} guesses. Good stuff!" if guessCount > 1 else "It took you one guess. Amazing!")

