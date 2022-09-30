"""Game where a player has to guess a random number"""
import numpy as np

#Generating a random number
number = np.random.randint(1,101)

#Counting the number of attempts it will take for the player to guess the number right
attempts = 0

#Creating a loop where the player has to repeatedly input a number and see whether he guessed correctly
while True:
    attempts += 1
    predicted_number = int(input("Input your predicted number: "))
    
    if predicted_number > number:
        print("Your number is larger than the random number, try again.")
        
    elif predicted_number < number:
        print("Your number is smaller than the random number")
        
    else:
        print(f"You guess the random number {number} in {attempts} attempts. Congrats!")
        break