from flask import Flask, render_template, request, Response, make_response, jsonify
from application.cleaner import clean
from application.controller.quiz_controller import generate_quiz 
from flask_cors import CORS, cross_origin

from question import QuestionGeneration

import json

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

generator = QuestionGeneration()

@app.route("/")
@cross_origin()
def index():
    resp = Response("Welcome to the Quiz Generator!", 200)
    return resp

@app.route("/content", methods=["POST"])
@cross_origin()
def receive_content():
    notes_content_py = json.loads(request.get_data().decode("utf-8"))  # type is list
    return generate_quiz(notes_content_py, generator).toJSON(), 200