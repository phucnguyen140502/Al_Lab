import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.datasets import load_iris # type: ignore

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                       columns=iris['feature_names'] + ['target'])

# Split the dataset into features (X) and labels (y)
X = iris_df.iloc[:, :-1]
y = iris_df.iloc[:, -1]

# Split the dataset into a balanced training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Visualize the first two features of the training set
plt.scatter(X_train.iloc[:, 0], X_train.iloc[:, 1], c=y_train, cmap='viridis')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')

# Add color bar
cbar = plt.colorbar()
cbar.set_ticks(np.unique(y_train))
cbar.set_ticklabels(iris.target_names)

plt.show()
