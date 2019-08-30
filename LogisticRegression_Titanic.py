import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers  = pd.read_csv("passengers.csv")
passengers.head()
passengers.describe()

##Clean the Data

# Update sex column to numerical
passengers['Sex'] = passengers['Sex'].map({'female':'1','male':'0'})
print(passengers.head())

# Fill the nan values in the age column
age_mean = passengers['Age'].mean()
passengers['Age'].fillna(value=age_mean, inplace = True)

# Create a first class column
passengers['FirstClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 1 else 0)

# Create a second class column
passengers['SecondClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 2 else 0)


## Select and Split the Data
# Select the desired features
features = passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']]
survival = passengers['Survived']

# Perform train, test, split
train_features, test_features, train_labels, test_labels = train_test_split(features, survival, test_size= 0.2, random_state  = 80)

##Normalize the Data
# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()
train_features = scaler.fit_transform(train_features)
test_features = scaler.transform(test_features)

##Create and Evaluate the Model
# Create and train the model
model = LogisticRegression()
model.fit(train_features, train_labels)

# Score the model on the train data
print(model.score(train_features, train_labels))

# Score the model on the test data
print(model.score(test_features, test_labels))

# Analyze the coefficients
coefficients = model.coef_
print(coefficients)

##Predict with the Model
# Sample passenger features
Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
Salik = np.array([0, 24, 0,0])

# Combine passenger arrays
sample_passengers = np.array([Jack, Rose, Salik])

# Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)

# Make survival predictions!
print(model.predict(sample_passengers))

# First Column Dying; Second Column #surviving
print(model.predict_proba(sample_passengers))
