# CS 109 Winter 2020 Contest
# Probabalistic Impacts in Intergenerational Mobility
# Author: Adonis Pugh	email: atrain@stanford.edu
# ------------------------------------------------
"""
This program implements computes a various conditional probabilities
related to intergenerational mobility, particularly attainment of higher
eduation, in regard to revevant background considerations including parent
income level, ethnicity, and rigor of high school eduation. The model
used in this program makes several salient and reasonable assumptions in
its Bayesian network. The dataset used in this program was obtained from
a publically available database at opportunityinsights.org, an organization
committed to producing reliable, long-term case studies related to
disrepancies in educational attainment.
"""
# ------------------------------------------------

import numpy as np

database = np.genfromtxt('mobility.csv', delimiter=',', dtype='str') #[:, (1:13, 28:32, 35:46, 53:66)]
discard = np.arange(12, 27).tolist() + np.arange(31, 34).tolist() + np.arange(41, 53).tolist() + np.arange(65, 69).tolist()
database = np.delete(database, discard, 1)
headers = database[0,:]
database = np.delete(database, 1, 0)

lower = 0 # lower class
lower_mid = 1 # lower-middle class
upper_mid = 2 # upper-middle class
upper = 3 # upper class

def discretize(db=database):
    for row in db:
        for i in range(row.length()):
            if :
                