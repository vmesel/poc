import os
import pandas as pd
from flask import Flask, jsonify


app = Flask(__name__)

# a simple page that says hello
@app.route('/')
def index():
    df = pd.read_csv("empenho_exemplo.csv", sep=";", encoding="iso-8859-1")
    
    return jsonify(df.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)