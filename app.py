from src.pipeline.predict_pipeline import PredictPipeline, CustomData

pipeline = PredictPipeline()

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
