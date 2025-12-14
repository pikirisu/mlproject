import os
import sys
import dill
import pickle

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.logger import logging
from src.exception import CustomException


def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_model(X_train, X_test, y_train, y_test, models, param):

    try:
        report = {}
        trained_models = {}

        for model_name, model in models.items():
            logging.info(f"Tuning model: {model_name}")

            if model_name == "CatBoosting Regressor":
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                score = r2_score(y_test, y_pred)
                report[model_name] = score
                trained_models[model_name] = model

                continue

            params_ = param.get(model_name, {})

            gs = GridSearchCV(
                estimator=model,
                param_grid=params_,
                cv=3,
                n_jobs=-1
            )

            gs.fit(X_train, y_train)

            best_model = gs.best_estimator_
            y_pred = best_model.predict(X_test)

            score = r2_score(y_test, y_pred)

            report[model_name] = score
            trained_models[model_name] = best_model

            logging.info(f"{model_name} R2 Score: {score}")

        return report, trained_models

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
