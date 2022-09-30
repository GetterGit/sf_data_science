"""Game where the computer has to guess a randomly generated number"""
import numpy as np

def random_predict(number:int=1) -> int:
    """
    This function prompts the computer to guess the random number and then tells him whether his assumption was correct

    Args:
        number (int, optional): the random number. Defaults to 1.

    Returns:
        int: number of attempts computer took to guess the number right
    """
    
    attempts = 0
    
    while True:
        attempts += 1
        
        #Computer guesses the random number
        predicted_number = np.random.randint(1,101)
        if predicted_number == number:
            break
    
    return attempts


def mean_attempts(random_predict) -> int:
    """
    This function launches the number-guessing algorithm for 1000 times and calculates 
    the mean of attempts required for the computer to guess the random number right in each iteration
    
    Args:
        random_predict ([type]): the function prompting computer to guess a given random number

    Returns:
        int: the mean of attempts for 1000 guessing iterations
    """
    
    #Creating list of storing the number of attempts for each of 1000 iterations
    attempts_per_iteration = []
    #Fixing the seed for reproducing the random numbers each launch rather than coming up with new random numbers
    np.random.seed(1)
    #Creating an array of 1000 random numbers
    random_array = np.random.randint(1,101,size=1000)
    
    for random_number in random_array:
        attempts_per_iteration.append(random_predict(random_number))
        
    mean = int(np.mean(attempts_per_iteration))
    
    print(f"The algorithm guesses the random number right in {mean} attempts on average")
    
mean_attempts(random_predict)
    
    

print(f"The random number is guessed correctly in {random_predict()} attempts!")