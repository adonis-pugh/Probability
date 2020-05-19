# Your Stanford email address: atrain@stanford.edu

"""
Starter code for Problem Set 3
for David Varodayan's Winter 2020
offering of CS109. Assembled by TA
Anand Shankar.
"""

# Do not add import statements.
# Do not remove this import statement either.
from numpy.random import rand

# part (a) - completed for you
def simulate_bernoulli(p=0.4):
    if rand() < p:
        return 1
    return 0


# part (b)
def simulate_binomial(n=20, p=0.4):
    success = 0
    for i in range(n):
    	if simulate_bernoulli(p) == 1:
    		success += 1
    return success


# part (c)
def simulate_geometric(p=0.03):
    trials = 1
    while simulate_bernoulli(p) != 1:
    	trials += 1
    return trials


# part (d)
def simulate_neg_binomial(r=5, p=0.03):
    trials = 1
    for i in range(5):
    	while simulate_bernoulli(p) != 1:
    		trials += 1
    return trials


# Note for parts (e) and (f):
# Since `lambda` is a reserved word in Python, we've used
# the variable name `lamb` instead. Do NOT use the word
# `lambda` in your code. It won't do what you want!


# part (e)
def simulate_poisson(lamb=3.1):
    success = 0
    ms = 60000
    prob = lamb / ms
    for i in range(ms):
    	if simulate_bernoulli(prob) == 1:
    		success += 1
    return success


# part (f)
def simulate_exponential(lamb=3.1):
	time = 1
	ms = 60000
	prob = lamb / ms
	while simulate_bernoulli(prob) != 1:
		time += 1
	return time / ms
    

def main():
    rv1 = simulate_bernoulli()
    print(f"simulate_bernoulli returned {rv1}")

    rv2 = simulate_binomial()
    print(f"simulate_binomial returned {rv2}")

    rv3 = simulate_geometric()
    print(f"simulate_geometric returned {rv3}")

    rv4 = simulate_neg_binomial()
    print(f"simulate_neg_binomial returned {rv4}")

    rv5 = simulate_poisson()
    print(f"simulate_poisson returned {rv5}")

    rv6 = simulate_exponential()
    print(f"simulate_exponential returned {rv6}")


if __name__ == "__main__":
    main()