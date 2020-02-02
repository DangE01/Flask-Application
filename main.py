# Copyright 2018 Google LLC
#
from flask import Flask
from flask import jsonify
import pandas as pd
import wikipedia
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types



app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello and welcome to my application'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a simple html page saying "Hello World"</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """
@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

@app.route('/wikipedia/<company>')
def wikipedia_route(company):
    result = wikipedia.summary(company, sentences=10)
    return result

@app.route('/nlp/<company>')
def nlp_route(company):
    result = wikipedia.summary(company, sentences=10)
    client = language.LanguageServiceClient()
    document = types.Document(
        content=result,
        type=enums.Document.Type.PLAIN_TEXT)
    entities = client.analyze_entities(document).entities
    return str(entities)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

