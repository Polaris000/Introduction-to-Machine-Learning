from sklearn.neighbors import KNeighborsClassifier

# helps predict the type of a data point based on the k nearest neighbours..
# the type of most of the neighbours decides the type of the data point.

 # features are the parameters by which basic objects such as the flower in the 
 # iris data_set are converted to numbers which can be used for prediction like
 # petal length and width and the sepal length and width.

 # data instance or sample or example is data that has some value for each
 # feature and can be used for interpretation.

 # features are represented conventionally by "X"
 # the target value is something that is the mission of the 
 # program.. in the iris dataset the targets are 0, 1 and 2 which are the 
 # indices of the flower species.

 # in regression the target is a numerical value(also called continuous) that
 # can be predicted based on the input

# import the iris dataframe
y = df["""target"""].values # response variable
X = df.drop("""target""", axis=1).values # feature array
# the drop() works by removing the target variable from the feature array
# the .values helps ensure that X and y are NumPy arrays


# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X, y)


# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))

#__________________

# Building a classifier to predict handwritten objects

# Import necessary modules
from sklearn import datasets
import matplotlib.pyplot as plt

# Load the digits dataset: digits
digits = datasets.load_digits()

# Print the keys and DESCR of the dataset
print(digits.keys())
print(digits.DESCR)

# Print the shape of the images and data keys
print(digits.images.shape)
print(digits.data.shape)

# Display digit 1010
plt.imshow(digits.images[1010], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

#_____________
# predict the label and calculate accuracy

# Import necessary modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Create feature and target arrays
X = digits.data
y = digits.target

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y)

# Create a k-NN classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=7)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Print the accuracy
print(knn.score(X_test, y_test))

# accuracy is 0.98!! damn
