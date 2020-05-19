# Do NOT add any other import statements.
# Don't remove these import statements.
import numpy as np
import copy

# Your Stanford email (fill in the blank): ___@stanford.edu

"""
Starter Code for CS 109 Problem Set 5
Assembled by TA Anand Shankar for David Varodayan's
Winter 2020 course offering.

*************************IMPORTANT*************************
For part_a and part_b, do NOT modify the name of 
the functions. Do not add or remove parameters to them
either. Moreover, make sure your return value is exactly as
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. 
You are free to write helper functions if you so desire.
Do NOT rename this file.
*************************IMPORTANT*************************
"""


def part_a(filename):
    """
    filename is the name of a data file, e.g. 
    "learningOutcomes.csv". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    Return the difference in sample means (float) as 
    described in the handout.
    """
    ### BEGIN YOUR CODE FOR PART (A) ###
    outcomes = np.genfromtxt(filename, delimiter=',', dtype='str')[:, 1:]
    first = outcomes[np.where(outcomes[:, 0] == "activity1")][:, 1].astype(float)
    second = outcomes[np.where(outcomes[:, 0] == "activity2")][:, 1].astype(float)

    return np.mean(first) - np.mean(second)
    ### END YOUR CODE FOR PART (A) ###
    
                                                  
def part_b(filename, seed=109):
    """
    filename is the name of a data file, e.g. 
    "learningOutcomes.csv". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    You MUST use np.random.choice with replace=True
    to draw random samples. You may NOT use any other 
    function to draw random samples. See assignment 
    handout for details.

    Return the p-value (float) as described in the handout.
    """
    np.random.seed(seed)  # DO NOT ALTER OR DELETE THIS LINE
    
    ### BEGIN YOUR CODE FOR PART (B) ###
    outcomes = np.genfromtxt(filename, delimiter=',', dtype='str')[:, 1:]
    first = outcomes[np.where(outcomes[:, 0] == "activity1")][:, 1].astype(float)
    second = outcomes[np.where(outcomes[:, 0] == "activity2")][:, 1].astype(float)
    size1 = first.size
    size2 = second.size
    obs_diff = abs(np.mean(first) - np.mean(second))
    both = np.concatenate((first, second))
    count = 0

    for i in range(0, 10000):
        sample1 = np.random.choice(both, size1, replace=True)
        sample2 = np.random.choice(both, size2, replace=True)
        diff = abs(np.mean(sample1) - np.mean(sample2))
        if diff >= obs_diff:
            count += 1

    return count / 10000
    ### END YOUR CODE FOR PART (B) ###
    

def optional_function(results, experience, seed=109):
    """
    We won't autograde anything you write in this function.
    But we've included this function here for convenience. 
    It will get called by our provided main method. Feel free
    to do whatever you want here, including leaving this function 
    blank. We won't read or grade it.
    
    """
    np.random.seed(seed)
    
    outcomes = np.genfromtxt(results, delimiter=',', dtype='str')[:, 1:]
    background = np.genfromtxt(experience, delimiter=',', dtype='str')
    both = np.append(outcomes, background, axis=1)
    both = np.delete(both, 2, 1)
    
    less = both[np.where(both[:,2] == "less")][:,:2]
    avg = both[np.where(both[:,2] == "average")][:,:2]
    more = both[np.where(both[:,2] == "more")][:,:2]
    
    for i in range(0,3):
        print("background " + str(i))
        if i == 0:
            arr = less
        if i == 1: 
            arr = avg
        if i == 2: 
            arr = more
        first = arr[np.where(arr[:, 0] == "activity1")][:, 1].astype(float)
        second = arr[np.where(arr[:, 0] == "activity2")][:, 1].astype(float)
        
        diff = np.mean(first) - np.mean(second)
        print("diff" + str(i) + " = " + str(diff))
        
        size1 = first.size
        size2 = second.size
        obs_diff = abs(np.mean(first) - np.mean(second))
        both = np.concatenate((first, second))
        count = 0
        
        for i in range(0, 10000):
            sample1 = np.random.choice(both, size1, replace=True)
            sample2 = np.random.choice(both, size2, replace=True)
            diff = abs(np.mean(sample1) - np.mean(sample2))
            if diff >= obs_diff:
                count += 1
        
        print("p-value = " + str(count / 10000))

                      
def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    print("****************************************************")
    print("Calling part_a with filename 'learningOutcomes.csv':")
    print("\tReturn value was:", part_a('learningOutcomes.csv'))
    print("****************************************************")

    print("****************************************************")
    print("Calling part_b with filename 'learningOutcomes.csv':")
    print("\tReturn value was:", part_b('learningOutcomes.csv'))
    print("****************************************************")

    print("****************************************************")
    print("Calling optional_function:")
    print("\tReturn value was:", optional_function('learningOutcomes.csv', 'background.csv'))
    print("****************************************************")


    print("Done!")


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statementmain()
if __name__ == "__main__":
    main()