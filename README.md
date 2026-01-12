## Student Performance Predictor
### Overview

The Student Performance Predictor is a simple end-to-end machine learning project that predicts a student’s writing score based on multiple academic and demographic factors.

The project covers the complete machine learning workflow, from data preprocessing and model training to deployment through a Flask web application. It was built as a learning project to understand how machine learning models are trained, evaluated, selected, and exposed through a user-facing interface.

### Problem Description

This project addresses a regression problem where the objective is to predict a numerical value (writing score) using a combination of numerical and categorical input features.

The model is currently trained only to predict writing score using other available factors such as reading score, math score, and background attributes.

### Features

- Predicts student writing score from user-provided inputs

- Supports both numerical and categorical features

- Trains multiple regression models and selects the best one

- Web-based interface built using Flask

- Accepts clean and structured user input through a form

### Machine Learning Approach

Multiple regression models are trained and evaluated on the dataset. The model with the best performance is automatically selected and used for inference in the application.

This multi-model approach helps compare different algorithms and understand their performance characteristics on the same problem.

### Input and Output
#### Input Features

The application accepts the following inputs through the web interface:

- Gender

- Race / Ethnicity

- Parental level of education

- Lunch type

- Test preparation course

- Reading score

- Math score

- Output

- Predicted writing score (numerical value)

### Web Application

The project includes a Flask-based web application that allows users to enter input values through a simple form and receive predictions in real time.

The UI is intentionally kept minimal and clean to focus on functionality rather than visual complexity.

### Project Setup
#### Prerequisites

- Python 3.10.18

- pip

- No GPU or special hardware is required.
