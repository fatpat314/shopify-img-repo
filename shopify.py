from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('app.html')
