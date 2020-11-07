from flask import Flask, render_template, request, session, Response, redirect
from database import connector
from model import entities
import pandas as pd
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods = ['POST'])
def post_form():
    c = json.loads(request.form['values'])
    form = entities.Form(
        name=c['name'],
        fullname=c['fullname'],
        phone=c['phone'],
        telephone=c['telephone']
    )
    session = db.getSession(engine)
    session.add(form)
    session.commit()
    return 'Created Form'

@app.route('/form/<id>', methods = ['GET'])
def get_template(id):
    return 0

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
