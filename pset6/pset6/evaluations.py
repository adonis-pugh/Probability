# pylint: disable = missing-function-docstring
'''
Written by Tim Gianitsos
CS 109 Probability for Computer Scientists, Fall 2019-2020, Winter 2019-2020
Tested with Python 3.7.5

*************************IMPORTANT*************************
NOTE TO STUDENTS: You do NOT need to modify this file.
Remember that you won't submit this file for autograding.
All of your work should go in the files listed for
submission on the assignment handout.

For instructions on how to run the code in this file, see
the README file in the starter code.
*************************IMPORTANT*************************
'''
import sys

import numpy as np

import utils
from naive_bayes import NaiveBayes
from logistic_regression import LogisticRegression

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_max_like_estm': True},
    dataset_name='simple',
    expected={(0, 0, 0): 2, (1, 0, 0): 1, (1, 1, 0): 1, (0, 1, 1): 2, (1, 0, 1): 1, (1, 1, 1): 1},
    message='Outputs the model the classifier learned from training'
)
def fit_bayes_simple(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_max_like_estm': True},
    dataset_name='netflix',
    expected={
        (0, 1, 1): 1497, (1, 1, 1): 1487, (2, 1, 1): 1325, (3, 1, 1): 1349, (4, 0, 1): 621,
        (5, 1, 1): 1354, (6, 1, 1): 1341, (7, 0, 1): 679, (8, 1, 1): 1922, (9, 0, 1): 762,
        (10, 1, 1): 1516, (11, 1, 1): 1476, (12, 1, 1): 1954, (13, 1, 1): 1498, (14, 1, 1): 1136,
        (15, 1, 1): 1151, (16, 0, 1): 558, (17, 0, 1): 649, (18, 0, 1): 563, (0, 0, 0): 940,
        (1, 0, 0): 718, (2, 0, 0): 736, (3, 0, 0): 779, (4, 0, 0): 981, (5, 1, 0): 1356,
        (6, 1, 0): 1412, (7, 1, 0): 1361, (8, 1, 0): 1957, (9, 0, 0): 688, (10, 1, 0): 1507,
        (11, 0, 0): 809, (12, 1, 0): 1987, (13, 1, 0): 1524, (14, 1, 0): 1286, (15, 1, 0): 1260,
        (16, 1, 0): 1726, (17, 1, 0): 1287, (18, 0, 0): 1560, (2, 0, 1): 906, (4, 1, 1): 1610,
        (5, 0, 1): 877, (6, 0, 1): 890, (9, 1, 1): 1469, (15, 0, 1): 1080, (18, 1, 1): 1668,
        (7, 1, 1): 1552, (16, 1, 1): 1673, (17, 1, 1): 1582, (3, 1, 0): 1490, (7, 0, 0): 908,
        (11, 1, 0): 1460, (18, 1, 0): 709, (1, 1, 0): 1551, (4, 1, 0): 1288, (5, 0, 0): 913,
        (6, 0, 0): 857, (9, 1, 0): 1581, (16, 0, 0): 543, (1, 0, 1): 744, (2, 1, 0): 1533,
        (13, 0, 0): 745, (11, 0, 1): 755, (13, 0, 1): 733, (15, 0, 0): 1009, (10, 0, 0): 762,
        (17, 0, 0): 982, (14, 0, 0): 983, (8, 0, 0): 312, (0, 1, 0): 1329, (0, 0, 1): 734,
        (3, 0, 1): 882, (10, 0, 1): 715, (14, 0, 1): 1095, (8, 0, 1): 309, (12, 0, 1): 277,
        (12, 0, 0): 282
    },
    message='Outputs the model the classifier learned from training'
)
def fit_bayes_netflix(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_max_like_estm': True},
    dataset_name='ancestry',
    message='Outputs the model the classifier learned from training'
)
def fit_bayes_ancestry(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_max_like_estm': True},
    dataset_name='heart',
    message='Outputs the model the classifier learned from training'
)
def fit_bayes_heart(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='simple',
    expected=np.round([-0.14577434, 0.82004294, -0.06660849], 2),
    message='Outputs the model the classifier learned from training'
)
def fit_logistic_simple(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 3000},
    dataset_name='netflix',
    expected=np.round([
        -1.26461287e+00, 1.46867021e-01, -3.21980376e-02, -1.92913294e-01,
        -1.11223178e-01, 3.28113677e-01, 3.16795785e-02, -1.11730732e-01,
        2.15760242e-01, -3.80626880e-02, -8.34949179e-02, 8.22010897e-02,
        4.84433141e-02, 2.07252764e-02, 1.06403162e-03, -1.05318507e-01,
        8.28210381e-03, -1.74354524e-02, 2.77574032e-01, 1.75611054e+00
    ], 2),
    message='Outputs the model the classifier learned from training'
)
def fit_logistic_netflix(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='ancestry',
    message='Outputs the model the classifier learned from training'
)
def fit_logistic_ancestry(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='heart',
    message='Outputs the model the classifier learned from training'
)
def fit_logistic_heart(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_max_like_estm': True},
    dataset_name='simple',
    expected=np.round(1.0, 2),
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_mle_simple(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_max_like_estm': False},
    dataset_name='simple',
    expected=np.round(1.0, 2),
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_laplace_simple(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_max_like_estm': True},
    dataset_name='netflix',
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_mle_netflix(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_max_like_estm': False},
    dataset_name='netflix',
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_laplace_netflix(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_max_like_estm': True},
    dataset_name='ancestry',
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_mle_ancestry(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_max_like_estm': False},
    dataset_name='ancestry',
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_laplace_ancestry(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_max_like_estm': True},
    dataset_name='heart',
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_mle_heart(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_max_like_estm': False},
    dataset_name='heart',
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_laplace_heart(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='simple',
    expected=np.round(1.0, 2),
    message='Percentage of correctly labeled answers:'
)
def predict_logistic_simple(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 3000},
    dataset_name='netflix',
    message='Percentage of correctly labeled answers:'
)
def predict_logistic_netflix(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='ancestry',
    message='Percentage of correctly labeled answers:'
)
def predict_logistic_ancestry(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='heart',
    message='Percentage of correctly labeled answers:'
)
def predict_logistic_heart(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

#pylint:disable=unused-argument
def fitting(clf, train_features, train_labels, test_features, test_labels):
    clf.fit(train_features, train_labels)
    return (
        clf.feature_counts if isinstance(clf, NaiveBayes)
        else clf.weights if isinstance(clf, LogisticRegression) else None
    )

def predictions(clf, train_features, train_labels, test_features, test_labels):
    clf.fit(train_features, train_labels)
    result_labels = clf.predict(test_features)
    assert len(test_labels) == len(result_labels)
    return (test_labels == result_labels).sum() / len(test_labels)

if __name__ == '__main__':
    utils.main(sys.argv[1:])
