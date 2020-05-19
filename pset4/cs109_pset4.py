# Do NOT add any other import statements.
# Don't remove this import statement.
import numpy as np

# Your Stanford email (fill in the blank): ___@stanford.edu

"""
Starter Code for CS 109 Problem Set 4
Assembled by TA Anand Shankar for David Varodayan's
Winter 2020 course offering.

*************************IMPORTANT*************************
For part_a and part_b, do NOT modify the name of the 
functions. Do not add or remove parameters to them either.
Moreover, make sure your return value is exactly as 
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. 
You are free to write helper functions if you so desire.
Do NOT rename this file.
*************************IMPORTANT*************************
"""


def part_a(filename):
    """
    filename is the name of a data file, e.g. 
    "personKeyTimingA.txt". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    Let X be a random variable as defined in the 
    assignment handout. You should compute and
    return E[X] (which is of type float).
    """
    
    key_data = np.genfromtxt(filename, delimiter=',', dtype=float)[:, 0]
    last = 0.0
    expect = 0.0
    prob = 1 / key_data.size
   
    for i in range (key_data.size):
        expect += (key_data[i] - last) * prob
        last = key_data[i]
    return expect
    	

def part_b(filename):

    """
    filename is the name of a data file, e.g. 
    "personKeyTimingA.txt". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    Let X be a random variable as defined in the 
    assignment handout. You should compute and
    return E[X^2] (which is of type float).
    """
    key_data = np.genfromtxt(filename, delimiter=',', dtype=float)[:, 0]
    last = 0.0
    expect_squared = 0.0
    prob = 1 / key_data.size
    print(key_data.size)
    for i in range (key_data.size):
        expect_squared += (key_data[i] - last)**2 * prob
        last = key_data[i]
    return expect_squared


def optional_function():
    """
    We won't autograde anything you write in this function.
    But we've included this function here for convenience. 
    It will get called by our provided main method. Feel free
    to do whatever you want here, including leaving this function 
    blank. We won't read or grade it.
    """
    pass  # TODO: delete this line and optionally implement the function!


def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    print("***********************************************************")
    print("    Calling part_a with filename 'personKeyTimingA.txt'    ")
    print("\tReturn value was:", part_a('personKeyTimingA.txt'))
    print("***********************************************************\n")

    print("***********************************************************")
    print("    Calling part_a with filename 'personKeyTimingB.txt'    ")
    print("\tReturn value was:", part_a('personKeyTimingB.txt'))
    print("***********************************************************\n")

    print("***********************************************************")
    print("    Calling part_b with filename 'personKeyTimingA.txt'    ")
    print("\tReturn value was:", part_b('personKeyTimingA.txt'))
    print("***********************************************************\n")

    print("***********************************************************")
    print("    Calling part_b with filename 'personKeyTimingB.txt'    ")
    print("\tReturn value was:", part_b('personKeyTimingB.txt'))
    print("***********************************************************\n")

    print("***********************************************************")
    print("                 Calling optional_function                 ")
    print("\tReturn value was:", optional_function())
    print("***********************************************************\n")

    print("Done!")


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
