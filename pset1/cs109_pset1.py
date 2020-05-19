# Name: Adonis Pugh

"""
*************** IMPORTANT *************** 
Do NOT rename this file. 
Do NOT rename the q16 function or alter its 
parameters in any way.

The autograder expects the following:
- Your file should be named cs109_pset1.py
- Your function should be named q16, and it 
  should take 2 arguments as indicated in the 
  provided starter code
- q16 must return a float
*************** IMPORTANT *************** 
"""

# Do NOT add any import statements
import numpy as np

# Instructions: 
# Fill in the following function.
# We will be testing your code by setting several random seeds.
# DO NOT ALTER THIS FUNCTION OUTSIDE THE BEGIN/END CODE MARKERS.
# You may add other helper functions if you wish.

def q16(seed: int = 37, ntrials: int = 100000) -> float:
    """
    Plays a game described in q16 ntrials times with a predetermined seed. 
    :param seed: seed for the numpy random number generator.
    :param ntrials: the number of trials to run.
    :return: the probability as described in the written pset.
    """
    np.random.seed(seed)
    #################### BEGIN CODE ####################
    # You MUST use the function np.random.randint from numpy
    # to generate random numbers, NOT random.randint or 
    # any other package.
    pass

    y_wins = 0

    for i in range(ntrials):
        sum = x = y = 0
        while sum <= 100:
            random = np.random.randint(1, 100)
            sum += random
            x = random
        while sum <= 200:
            random = np.random.randint(1, 100)
            sum += random
            y = random
        if y > x:
            y_wins += 1

    prob = y_wins / ntrials
    return prob

    ####################  END CODE  ####################


