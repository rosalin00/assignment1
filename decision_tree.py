#-------------------------------------------------------------------------
# AUTHOR: Alondra Marin
# FILENAME: decision_tree.py
# SPECIFICATION: A small description of the program would be, that it first begins with reading a CSV file named
# 'contact_lens.csv' and preprocesses it, converting categorical values into numerical representations. This data is
# then used to train a decision tree classifier with an entropy-based criterion for splitting nodes.The code then
# generates a visual representation of the trained decision tree.
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment it took me a few days mostly the whole week
# to complete this assignment.
#-----------------------------------------------------------*/
#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
#AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays
#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []
#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            db.append (row)
            print(row)
#transform the original categorical training features into numbers and add to the
#4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
for row in db:
    xDataRow = []
    for i, value in enumerate(row):
        if i == 0: xDataRow.append(1 if value  == 'Young' else 3 if value == 'Prepresbyopic' else 3)
        elif i == 1: xDataRow.append(1 if value == 'Myope' else 2)
        elif i == 2: xDataRow.append(1 if value == 'No' else 2)
        elif i == 3: xDataRow.append(1 if value == 'Reduced' else 2)
    X.append(xDataRow)
# X =
#transform the original categorical training classes into numbers and add to the
#vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =
for row in db:
    Y.append(1 if row[-1] == 'Yes' else 2)
#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)
#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'],
class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
