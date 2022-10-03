""" The "Guess a number" game where computer chooses a random number and then guesses it"""


import numpy as np


def random_predict(number: int = np.random.randint(1, 101)) -> int:
    """
    This function makes computer guess the randomly generated number with the quality metrics being no more than 20 attempts

    Args:
        number (int, optional): the randomly generated number for computer to guess. Defaults to np.random.randint(1, 101).

    Returns:
        int: the number of attempts required to guess the random number right
    """
    attempts = 0
    # Generating a list from 1 to 100 which we'll use for minimizing attempts
    lst_number = list(range(1, 101))

    while True:
        attempts += 1
        # We always choose the mean of the list to cut it in half if predicted_number != number
        predicted_number = int(np.mean(lst_number))
        # We find an index of either the number in the middle of the list or the first of two numbers in the middle
        # We then use this index to cut the list in half if predicted_number != number
        half = int(len(lst_number) / 2)
        if predicted_number == number:
            break
        elif predicted_number < number:
            lst_number = lst_number[half:]
        elif predicted_number > number:
            lst_number = lst_number[:half]

    return attempts


def mean_attempts(random_predict) -> int:
    """
    This function generates an array of 1000 randon numbers from 1 to 100 and then passes those random numbers
    one-by-one to the random_predict function to find a number of attempts required from computer to guess
    the random number right.

    Then, the function finds the mean of all required attempts across 1000 iterations which has a quality metric of
    being less than 20.

    Args:
        random_predict ([type]): this is a function prompting computer to guess the passed random number and return
        the number of attempts taken to guess it right

    Returns:
        int: mean number of attempts to guess the ranom number right across 1000 iterations
    """
    # Creating an empty list to store returted attempts for 1000 iterations
    iter_attempts = []
    random_numbers = np.random.randint(1, 101, size=1000)

    for number in random_numbers:
        iter_attempts.append(random_predict(number))

    mean = int(np.mean(iter_attempts))

    return mean, iter_attempts


# Launching the program to QA
mean, iter_attempts = mean_attempts(random_predict)
print(f"It took {mean} attempts on average to guess the random number right.")
print(f"It's less than 20 attempts by {20 - mean}.") if 20 > mean else print(
    f"Wrong solution! The mean is larger than 20 by {mean - 20}."
)

# I was also not sure if you meant "<20 attempts on average" or "<20 per iteration"
# So, adding an extra check
print(
    "It took less than 20 attempts to guess the random number across all iterations."
) if len(list(filter(lambda x: x >= 20, iter_attempts))) == 0 else print(
    "Wrong solution! There's an iter with 20 attempts or more."
)
