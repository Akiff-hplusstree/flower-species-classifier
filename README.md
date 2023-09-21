# Flower Species Classifier

A Python application that uses a Random Forest classifier to predict the species of a flower based on its sepal and petal measurements.

## Table of Contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Description

This project is a flower species classifier that uses a Random Forest classifier trained on the Iris dataset. Given the sepal length, sepal width, petal length, and petal width of a flower, it predicts its species as one of the following: Setosa, Versicolor, or Virginica.

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.10 or later
- Required Python libraries (installed via `requirement.txt`):
  - numpy
  - pandas
  - scikit-learn
  - joblib

## Installation

To set up the Flower Species Classifier, follow these steps:

1. Clone this repository to your local machine:

```bash
   git clone https://github.com/yourusername/flower-species-classifier.git
   cd flower-species-classifier
```
2. Create a virtual environment (recommended):

```bash
    python3 -m venv venv
    source venv/bin/activate
```

3. Install the required Python libraries:

```bash
    pip install -r requirement.txt
```

## Usage

To use the Flower Species Classifier, run the main.py script as follows:

```bash
python3 main.py
```
The script will prompt you to enter the sepal and petal measurements for a flower. After entering the measurements, it will predict the flower species and display the result.

## Examples

Here's an example of how to use the Flower Species Classifier:

```bash
Please enter the following features:
Sepal Length (cm): 5.1
Sepal Width (cm): 3.5
Petal Length (cm): 1.4
Petal Width (cm): 0.2
The predicted flower species is: Setosa
```

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

Fork the repository on GitHub.
Create a new branch for your feature or bug fix.
Make your changes and test them thoroughly.
Submit a pull request with a clear description of your changes.

