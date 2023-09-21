# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the Iris dataset
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Save the trained model to a file (optional)
joblib.dump(rf_classifier, 'rf_model.pkl')

# Load the trained model (if available)
# rf_classifier = joblib.load('rf_model.pkl')

# Prompt the user for input features
print("Please enter the following features:")
sepal_length = float(input("Sepal Length (cm): "))
sepal_width = float(input("Sepal Width (cm): "))
petal_length = float(input("Petal Length (cm): "))
petal_width = float(input("Petal Width (cm): "))

# Use the trained model to predict the flower species
input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
predicted_species = rf_classifier.predict(input_features)

# Display the predicted flower species to the user
if predicted_species == 0:
    flower_name = "Setosa"
elif predicted_species == 1:
    flower_name = "Versicolor"
else:
    flower_name = "Virginica"

print(f"The predicted flower species is: {flower_name}")
