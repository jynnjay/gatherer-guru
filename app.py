from flask import Flask, render_template, url_for, redirect, request
import csv
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
