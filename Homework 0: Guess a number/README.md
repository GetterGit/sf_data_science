# Homework 0: Guess a number

## Outline

[1. Project description](https://github.com/GetterGit/sf_data_science/blob/main/Homework%200:%20Guess%20a%20number/README.md#Project-description)

[2. Case solved](https://github.com/GetterGit/sf_data_science/blob/main/Homework%200:%20Guess%20a%20number/README.md#Case-solved)

[3. Brief data overview](https://github.com/GetterGit/sf_data_science/blob/main/Homework%200:%20Guess%20a%20number/README.md#Brief-data-overview)

[4. Project stages](https://github.com/GetterGit/sf_data_science/blob/main/Homework%200:%20Guess%20a%20number/README.md#Project-stages)

[5. Results](https://github.com/GetterGit/sf_data_science/blob/main/Homework%200:%20Guess%20a%20number/README.md#Results)

[6. Conclusions](https://github.com/GetterGit/sf_data_science/blob/main/Homework%200:%20Guess%20a%20number/README.md#Conclusions)

### 1. Project description

A number-guessing game where computer has to guess a randomly generated number in less than 20 attempts.

### 2. Case solved

We need to write a program which guesses a randomly generated number for less than 20 attempts.

**Conditions:**

- Computer chooses a random number from 0 to 100, and either a human or computer has to guess this number.
- The guessing algorithm evaluates whether each guessed number is larger, smaller or equal to the random number chosen by the computer and adjusts the next guess accordingly.

**Quality metric:**

- The results are evaluated based on the average number of attempts required to guess the random number right during 1000 iterations.
- Due to subjectively ambiguous task explanation, another metric was added: each iteration should take less than 20 attempts to guess the random number right.

**Learning curve:**

- How to write a clean and well-documented code.

:arrow_up:[back to outline](https://github.com/GetterGit/sf_data_science/blob/main/Homework%200:%20Guess%20a%20number/README.md#Outline)

### 3. Brief data overview

- N/A

### 4. Project stages

- Develop a simple algorithm cutting the list of potential random numbers in half based on whether the current guess is smaller or larger than the actual random number.
- Code the algorithm.
- QA the algorithm throughout 1000 iterations.

### 5. Results

- The algorithm which finds a random number from 1 to 100 it less than 20 attempts.

### 6. Conclusions

- Learned how to critically analyze tech requirements.
- Learned how to write a readable and reproduceable code.
- Learned how to document the code.
- Learned some of PEP8 basics.

:arrow_up:[back to outline](https://github.com/GetterGit/sf_data_science/blob/main/Homework%200:%20Guess%20a%20number/README.md#Outline)
