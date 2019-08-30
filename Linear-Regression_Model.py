import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")

#Data Explore
df.head();

#Total Production of Honey per year
prod_per_year = df.groupby('year').totalprod.mean().reset_index()
#Year
X = prod_per_year["year"]
X = X.values.reshape(-1, 1)
#Total Honey Production
y = prod_per_year["totalprod"]

#Year vs Production
plt.scatter(y, X)
plt.show()

#Linear Regression
regr = LinearRegression()

regr.fit(X, y)
print(regr.coef_[0])
print(regr.intercept_)

#Predict Y Values
y_predict = regr.predict(X)

#Year vs Production
plt.scatter(y_predict, X)
plt.show()

# Future Prediction based on Model
X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1, 1)

future_predict = regr.predict(X_future)

#Plot Future data
plt.plot(future_predict, X_future)
plt.show()
