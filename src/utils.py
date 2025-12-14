import os
import sys 

import numpy as np
import pandas as pd
import dill

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.logger import logging
from src.exception import CustomException

def save_obj(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok = True)
        
        with open (file_path, "wb") as file_obj:
            dill.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)

def evaluate_model(X_train, X_test, y_train, y_test, models,param):
    try:
        report = {}
        
        for model_name, model in models.items():
            if model_name == "CatBoosting Regressor":
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)
                score = r2_score(y_test, y_pred)
                report[model_name] = score
                continue
            params_ = param.get(model_name, {})
            gs = GridSearchCV(model, params_, cv=3)
            gs.fit(X_train, y_train)
            
            best_model = gs.best_estimator_
            y_pred = best_model.predict(X_test)

            
            score = r2_score(y_test, y_pred)
            report[model_name] = score
            
        return report

    except Exception as e:
        raise CustomException(e,sys)