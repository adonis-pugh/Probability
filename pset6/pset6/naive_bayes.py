'''
Naive Bayes Classifier
'''
# Do NOT add any other import statements.
# Don't remove this import statement.
import numpy as np
# Your Stanford email (fill in the blank): atrain@stanford.edu

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

class NaiveBayes:
    '''
    Naive Bayes Classifier

    For a datapoint, the Naive Bayes classifier computes the probability of each label,
    and then it predicts the label with the highest probability. During training,
    it learns probabilities by counting the occurences of feature/label combinations
    that it finds in the training data. During prediction, it uses these counts to
    compute probabilities.
    '''

    def __init__(self, use_max_like_estm):
        '''
        DO NOT RENAME INSTANCE VARIABLES. You don't need to change anything
        in this method.
        '''
        self.label_counts = {0: 0, 1: 0}
        self.feature_counts = {}
        self.use_max_like_estm = use_max_like_estm # alternative signifies using Laplace MAP

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

        Set the instance variable `self.label_counts` to a Python dictionary
        which maps labels to their frequencies. There will be EXACTLY two keys
        corresponding to the two labels of 0 and 1.

        i.e.
        The key is a number
            label (0 or 1 from our data)
        The value is a number
            frequency

        e.g.
        Consider the dictionary {0: 122, 1: 324}
        The label 0 occured 122 times and the label 1 occured 324 times.

        ================================
        Instruction:

        Set the instance variable `self.feature_counts` to a Python dictionary
        which maps tuples of feature/label combinations to their frequencies.

        i.e.
        The key is a tuple of 3 numbers.
            (column number, feature value, label)
        The value is a number:
            frequency

        e.g.
        Consider the dictionary {(3, 1, 0): 17, (7, 0, 1): 2, ...}
        Column 3 with a value of 1 and output label of 0 occurred 17 times in the training data
        Column 7 with a value of 0 and output label of 1 occurred 2 times in the training data
        (there will be many others)

        ================================
        Hints:

        - These counts are NOT affected by the value of `self.use_max_like_estm`.
        - Remember you are not returning any values; rather, you will set the values of
        the instance variables self.label_counts and self.feature_counts as described above.

        '''
        ### YOUR CODE HERE (~5-10 Lines)
        for i in range(len(train_labels)): 
             if train_labels[i] == 0: self.label_counts[0] += 1
             else:  self.label_counts[1] += 1
             
        for row in range(train_features.shape[0]):
            for col in range(train_features.shape[1]):
                key = (col, train_features[row][col], train_labels[row])
                self.feature_counts[key] = self.feature_counts.get(key, 0) + 1
        ### END YOUR CODE

    def predict(self, test_features):
        '''
        ================================
        Parameters:

        `test_features`: a 2D numpy array of shape n x d where rows represent
            the n samples and columns represent the d features

        ================================
        Instructions:

        Given n rows of features, return a numpy array `preds` of length n (initialized
        for you to all 0's) so that `preds[i]` contains the classifier's prediction for
        sample i. This involves looping through each row in test_features, computing
        the probability that a given row is a 1 and computing the probability that the
        row is a 0. Then, assign the corresponding element in the output array `preds`
        to a 0 or 1 depending on which probability was higher.

        ================================
        Hints:
        - You will be making use of the counts that you computed in the fit method to
        compute the probability of each row.
        - The boolean variable `self.use_max_like_estm` affects this computation.

        '''
        preds = np.zeros(test_features.shape[0], dtype=np.uint8)
        ### YOUR CODE HERE (~10-30 Lines)
        fix = 0 if self.use_max_like_estm else 1
        prob_no = (self.label_counts[0] + fix) / (self.label_counts[0] + self.label_counts[1] + (2 * fix))
        prob_yes = 1 - prob_no
        for sample in range(test_features.shape[0]):
            prob_feature_no = prob_feature_yes = 1
            for feature in range(test_features.shape[1]):
                value = test_features[sample][feature]
                prob_feature_no *= (self.feature_counts.get((feature, value, 0), 0) + fix) / (self.label_counts[0] + (2 * fix))
                prob_feature_yes *= (self.feature_counts.get((feature, value, 1), 0) + fix) / (self.label_counts[1] + (2 * fix))
            preds[sample] = 0 if (prob_feature_no * prob_no) > (prob_feature_yes * prob_yes) else 1
        ### END YOUR CODE
        return preds
