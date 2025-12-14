from flask import Flask, render_template, request
import pandas as pd
import pickle
import os
import sys

from src.logger import logging
from src.exception import CustomException
from src.pipeline.prediction_pipeline import PredictPipeline, CustomData

pipeline = PredictPipeline()
app = Flask(__name__)

MODEL_PATH = os.path.join("artifacts", "model.pkl")
PREPROCESSOR_PATH = os.path.join("artifacts", "preprocessor.pkl")

try:
    model = pickle.load(open(MODEL_PATH, "rb"))
    preprocessor = pickle.load(open(PREPROCESSOR_PATH, "rb"))
    logging.info("Model and preprocessor loaded successfully")
except Exception as e:
    raise CustomException(e, sys)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = CustomData(
            gender=request.form["gender"],
            race_ethnicity=request.form["race_ethnicity"],
            parental_level_of_education=request.form["parental_level_of_education"],
            lunch=request.form["lunch"],
            test_preparation_course=request.form["test_preparation_course"],
            reading_score=int(request.form["reading_score"]),
            math_score=int(request.form["math_score"]),
        )

        df = data.get_data_as_dataframe()
        prediction = pipeline.predict(df)[0]

        return render_template("result.html", prediction=round(prediction, 2))

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
