import os
import pandas as pd
from flask import Flask, jsonify


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    df = pd.read_csv("empenho_exemplo.csv", encoding='ISO-8859-1', sep=";")
    df = df.fillna("-")
    return jsonify(df.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)