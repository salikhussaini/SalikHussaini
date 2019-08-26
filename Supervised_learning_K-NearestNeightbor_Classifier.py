from sklearn.datasets import load_breast_cancer 
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#Load Data
breast_cancer_data = load_breast_cancer()

#Print first Tuple
print (breast_cancer_data.data[0])
#Print Variables
print (breast_cancer_data.feature_names)
#print target variable
print (breast_cancer_data.target, breast_cancer_data.target_names)

#Splitting the data into Training and Validation Sets 
training_data, validation_data , training_labels, validation_labels = train_test_split(
  breast_cancer_data.data, breast_cancer_data.target, 
  test_size = 0.2, random_state = 80)

print (training_data.shape)
print (training_labels.shape)

#Create Classifier
classifier = KNeighborsRegressor(n_neighbors = 9)
#Fit the data
classifier.fit(training_data, training_labels)
#Score the Classifier 
print(classifier.score(validation_data, validation_labels))

#Which K is ideal?
accuracy = []
for k in range(1, 101):
  klist = []
  #Create classifier
  classifier = KNeighborsRegressor(n_neighbors = k)
  #Train classifier
  classifier.fit(training_data, training_labels)
  #Report accuracy
  accuracy.append(classifier.score(validation_data, validation_labels))
  
print (accuracy)
k_list = range(1, 101)

plt.plot(k_list, accuracy)
plt.xlabel('k')
plt.ylabel('validation accurarcy')
plt.title('Breast cancer classifier accuracy')
plt.show()
