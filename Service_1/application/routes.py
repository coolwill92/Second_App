from application import app
from flask import render_template, request
import requests
import random
import os


@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/randomword')
    sentence = response.text
    return render_template('index.html', sentence = sentence, title = 'Home')