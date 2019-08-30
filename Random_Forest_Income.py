def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

##Investigate The Data
income_data  = pd.read_csv("income.csv", header = 0, delimiter = ", ")
print(income_data.iloc[0])

#Column addition
income_data["sex-int"] = income_data["sex"].apply(lambda row: 0 if row == "Male" else 1)

income_data["country-int"] = income_data["native-country"].apply(lambda row: 0 if row == "United-States" else 1)

##Format The Data For Scikit-learn
labels = income_data["income"]
data = income_data[["age", "capital-gain", "capital-loss", "hours-per-week", "sex-int", "country-int"]]

#Train Test Split 
train_features, test_features, train_labels, test_labels = train_test_split(data, labels, test_size= 0.2, random_state  = 1)

##Create The Random Forest
forest = RandomForestClassifier(random_state = 1)

#train model
forest.fit(train_features, train_labels)

#Print Model Results
print(forest.score(test_features, test_labels))
