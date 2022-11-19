from flask import Flask, render_template, request
from application.cleaner import clean
from application.controller.quiz_controller import generate_quiz 
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/content", methods=["POST"])
def receive_content():
    notes_content = clean(request.get_data().decode("utf-8"))
    print(f"Received data: {notes_content}")
    return generate_quiz(notes_content).toJSON(), 200