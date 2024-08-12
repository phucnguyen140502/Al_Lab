import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.linear_model import Perceptron # type: ignore
from sklearn.metrics import accuracy_score # type: ignore

data_url = "iris.data"  # Replace with the actual path of the downloaded iris.data file
column_names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
iris_df = pd.read_csv(data_url, names=column_names)

features = iris_df[['sepal length', 'sepal width']].values
labels = iris_df['class'].values

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, stratify=labels, random_state=42)

# Filter the training set to include only 'setosa' and 'versicolor' classes
train_set = pd.DataFrame(np.column_stack((X_train, y_train)), columns=['sepal length', 'sepal width', 'class'])
filtered_train_set = train_set[train_set['class'].isin(['Iris-setosa', 'Iris-versicolor'])]

# Create scatter plot
setosa = filtered_train_set[filtered_train_set['class'] == 'Iris-setosa']
versicolor = filtered_train_set[filtered_train_set['class'] == 'Iris-versicolor']
plt.scatter(setosa['sepal length'], setosa['sepal width'], c='purple', label='Setosa')
plt.scatter(versicolor['sepal length'], versicolor['sepal width'], c='yellow', label='Versicolor')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')

# Add color bar for classification
classes = ['setosa', 'versicolor']
colors = ['purple', 'yellow']
scatter = plt.scatter([], [], c=[], cmap='viridis')
cbar = plt.colorbar(scatter, ticks=[0, 1])
cbar.set_ticklabels(classes)

plt.show()

perceptron = Perceptron()
perceptron.fit(X_train, y_train)
y_train_pred = perceptron.predict(X_train)
y_test_pred = perceptron.predict(X_test)

train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)
train_error = 1 - train_accuracy
test_error = 1 - test_accuracy

print("Training Error: ", train_error)
print("Test Error: ", test_error)