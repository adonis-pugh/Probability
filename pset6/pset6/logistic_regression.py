'''
Logistic Regression Classifier
'''
# Do NOT add any other import statements.
# Don't remove this import statement.
import numpy as np
# Your Stanford email (fill in the blank): ___@stanford.edu

"""
Starter Code for CS 109 Problem Set 6
Assembled by TAs Tim Gianitsos, Alex Tsun, and Anand Shankar
for David Varodayan's Winter 2020 course offering.

*************************IMPORTANT*************************
Do NOT modify the name of any functions. Do not add or remove
parameters to them either. Moreover, make sure your return
value is exactly as described in the PDF handout and in the
provided function comments. Remember that your code is being
autograded. You are free to write helper functions if you so
desire but they are not necessary. Do NOT rename this file.
Do NOT modify any code outside the begin and end code markers.
*************************IMPORTANT*************************
"""

def sigmoid(vec):
    '''
    Parameters:

    `vec`: a numpy array or scalar
    ================================
    Returns the sigmoid function applied to each element of `vec`.
    '''
    return 1 / (1 + np.exp(-vec))

class LogisticRegression:
    '''
    Logistic Regression Classifier

    For a datapoint, the Logistic Regression classifier computes the probability of each label,
    and then it predicts the label with the highest probability. During training, it learns
    weights for each feature using gradient ascent. During prediction, it uses the test data
    to apply a linear transformation to the weights.
    '''

    def __init__(self, learning_rate, max_steps):
        '''
        DO NOT RENAME INSTANCE VARIABLES. You don't need to change
        anything in this method.
        '''
        self.learning_rate = learning_rate
        self.max_steps = max_steps
        self.weights = None

    def fit(self, train_features, train_labels):
        '''
        ================================
        Parameters:

        `train_features`: a 2D numpy array of shape n x d where rows represent
            the n samples and columns represent the d features
        `train_labels`: a 1D numpy array of shape n where each value corresponds
            to the correct label for a respective row in `train_features`

        ================================
        Instruction:

        Update the theta vector by performing gradient ascent.
        You should iterate `self.max_steps` times, and for every gradient you
        compute, you should scale it by `self.learning_rate`.

        ================================
        Hints:
        - You will want to make use of the provided sigmoid function.
        - This takes some time to execute on the Netflix dataset if you implement
        it using multiple loops and sums, but it takes only a few moments if you use
        matrix multiplication. It also reduces the lines of code to write. However, don't
        use matrix multiplication if you are uncomfortable with it.
        - You can do matrix multiplication in numpy using np.matmul (or by using
        the `@` symbol). That is, `A @ B` will return the matrix-matrix product AB,
        and `A @ x` will return the matrix-vector product Ax.
        '''

        # This line inserts a column of ones before the first column of train_features,
        # resulting in the an `n x (d + 1)` size matrix, This is so we
        # don't need to have a special case for the bias weight.
        train_features = np.insert(train_features, 0, 1, axis=1)

        # This makes the matrix immutable
        train_features.setflags(write=False)

        # This is the theta you will be performing gradient ascent on. It has
        # shape (d + 1).
        theta = np.zeros(train_features.shape[1])

        ### YOUR CODE HERE (~3-10 Lines)
        for i in range(self.max_steps):
            theta += self.learning_rate * ((train_labels - sigmoid(train_features @ theta)) @ train_features)
        ### END YOUR CODE
        self.weights = theta

    def predict(self, test_features):
        '''
        ================================
        Parameters:

        `test_features`: a 2D numpy array of shape n x d where rows represent
            the n samples and columns represent the d features

        ================================
        Instruction:

        Given n rows of features, return a numpy array `preds` of length n (initialized
        for you to all 0's) so that `preds[i]` contains the classifier's prediction for
        sample i. This involves applying the weights we learned in the fit() method.

        ================================
        Hints:
        - The remaining functionality can be written in few lines if you take advantage
        of matrix multiplication, but this is not required.
        '''

        test_features = np.insert(test_features, 0, 1, axis=1) # add bias term
        test_features.setflags(write=False) # make immutable
        preds = np.zeros(test_features.shape[0])
        ### YOUR CODE HERE (~1-7 Lines)
        preds = [1 if sigmoid(test_features[i, :] @ self.weights) > 0.5 else 0 for i in range(test_features.shape[0])]
        ### END YOUR CODE
        return preds
