# CS 109 Probability for Computer Scientists

Machine Learning Classifier Assignment

## Acknowledgements

Quarters:
* Autumn 2019-2020 (Professor Lisa Yan)
* Winter 2019-2020 (Professor David Varodayan)

Authors:
* [Tim Gianitsos](https://github.com/timgianitsos) - classifiers, solution code, questions, evaluations
* [Anand Shankar](https://github.com/anandshankar7) - autograder, instructions
* [Alex Tsun](https://github.com/alextsun) - comments, repo maintenance
* [Chris Piech](https://github.com/chrispiech) - datasets (compiled prior to autumn 2019-2020)

## Instructions

1. In `naive_bayes.py`, implement the Naive Bayes Classifier methods where you see `YOUR CODE HERE`.

1. In `logistic_regression.py`, implement the Logistic Regression Classifier methods where you see `YOUR CODE HERE`.

Make sure to follow the instructions in the comments of those files and in the assignment handout.

## Notes

**Ensure you are using `python` >= 3.6**

1. Check the outputs of your classifiers on each of the datasets:
	```
	python evaluations.py
	```

	Test individual functions:
	```
	python evaluations.py predict_bayes_mle_simple fit_logistic_heart
	```

1. Run functions manually. Note that you don't need to pass in the classifiers or datasets - the `python` decorator takes care of these parameters for you.
	```
	>>> import evaluations
	>>> evaluations.predict_bayes_mle_ancestry()
	```
	Silence output:
	```
	>>> import evaluations
	>>> evaluations.predict_bayes_mle_ancestry(display_question=False)
	```

1. Play around with your classifiers:
	```
	>>> import numpy as np
	>>> from naive_bayes import NaiveBayes
	>>> n = NaiveBayes(use_max_like_estm=True)
	>>> n.fit(np.array([[0,0,0,0], [1,1,1,1], [1,0,1,0]]), np.array([1, 0, 1]))
	>>> n.predict(np.array([[0,1,0,1], [1,0,1,0]]))
	array([0, 1], dtype=uint8)
	```

## Setup (for teaching assistants)

Only release the following files to students:
* `README.md`
* `datasets/`
* `evaluations.py`
* `logistic_regression.py`
* `naive_bayes.py`
* `utils.py`
