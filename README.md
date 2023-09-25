# Flower Species Classifier

A Python application that uses a Random Forest classifier to predict the species of a flower based on its sepal and petal measurements.

## Table of Contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)

## Description

This project is a flower species classifier that uses a Random Forest classifier trained on the Iris dataset. Given the sepal length, sepal width, petal length, and petal width of a flower, it predicts its species as one of the following: Setosa, Versicolor, or Virginica.

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.10 or later
- Required Python libraries (installed via `requirements.txt`):
  - numpy
  - pandas
  - scikit-learn
  - joblib

## Installation

To set up the Flower Species Classifier, follow these steps:

1. Clone this repository to your local machine:

```bash
   git clone https://github.com/Akiff-hplusstree/flower-species-classifier.git
   cd flower-species-classifier
```
2. Create a virtual environment (recommended):

```bash
    python3 -m venv venv
    source venv/bin/activate
```

3. Install the required Python libraries:

```bash
    pip install --no-cache-dir -r requirements.txt
```

## Usage

To use the Flower Species Classifier, run the `main.py` script as follows:

```bash
python3 main.py
```

The script will create a `rf_model.pkl` file which will store the trained model. The script will prompt you to enter the sepal and petal measurements for a flower. After entering the measurements, it will predict the flower species and display the result.

You can also use the classifier with docker and docker-compose. Remember to first run the `main.py` in order to store the trained model.

### Using Docker:

To run the Flower Species Classifier using Docker, follow these steps:

1. Build and run the Docker image for the application using the provided Dockerfile:

```bash
docker build -t flower-classifier .
```

2. Run the Docker container:

```bash
docker run -it --rm flower-classifier
```

This command will start the application inside a Docker container. Follow the prompts to enter the sepal and petal measurements for a flower, and it will predict the flower species.

### Using Docker Compose

Alternatively, you can use Docker Compose to simplify the deployment:

1. Make sure you have Docker Compose installed on your system. If not, Install it with the following command:

```bash
# Install Docker Compose on Linux
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Apply executable permissions
sudo chmod +x /usr/local/bin/docker-compose
```
2. Use the following docker-compose.yml configuration:

```yaml
version: '3'

services:
  flower-species-classifier:
    build:
      context: .
    image: flower-classifier:latest
    container_name: flower-classifier
    command: ["python3", "main.py"]
```

Run the Docker Compose command to build and start the application:

```bash
docker-compose run flower-species-classifier
```
This will create and run the Flower Species Classifier container.

Both methods will allow you to interact with the Flower Species Classifier using Docker, making it easy to use and deploy in a containerized environment.

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

