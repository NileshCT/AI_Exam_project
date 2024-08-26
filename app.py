from flask import Flask,request
import numpy as np
import pickle
import json as json
import flasgger
from flasgger import Swagger

"""from flasgger import Swagger: 
This line is importing the Swagger 
class from the flasgger module. Swagger 
is a set of open-source tools built around 
the OpenAPI Specification that can help you design, 
build, document and consume REST APIs."""

app=Flask(__name__)
# This line is creating an instance of the Flask class.
"""The argument __name__ is a special 
variable in Python that is automatically 
set to the name of the module in which it is used"""
Swagger(app)
# it’s a great tool for designing and testing APIs.
#creating swagger instance
#it add swagger ui to flask app

import pickle

# Open the file in binary mode for reading
pick = open('model2.pkl', 'rb')

# Use pickle.load to load the data
model= pickle.load(pick)


@app.route("/predict",methods=["GET"])
def predict_class():
    Age=int(request.args.get("Age"))
    BS_Fast=int(request.args.get("BS_Fast"))
    BS_pp=int(request.args.get("BS_pp"))
    Plasma_R=int(request.args.get("Plasma_R"))
    Plasma_F=int(request.args.get("Plasma_F"))
    HbA1c=int(request.args.get("HbA1c"))
    Normal=int(request.args.get("Normal"))
    Type1=int(request.args.get("Type1"))
    Type2=int(request.args.get("Type2"))
    prediction=model.predict([[Age,BS_Fast,BS_pp,Plasma_R,Plasma_F,HbA1c,Normal,Type1,Type2]])
    print(prediction[0])
    return "Model prediction is"+str(prediction)



@app.route('/predict_file',methods=["POST"])

def prediction_test_file():
    import pandas as pd
    X_test=pd.read_csv(request.files.get("file"))
    prediction=model.predict(X_test)
    return str(list(prediction))
if __name__=="__main__":
    app.run(debug=True)
