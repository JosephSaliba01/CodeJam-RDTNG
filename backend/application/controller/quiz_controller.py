from application.model import Quiz, Question

def generate_quiz(content: str):
    question1 = Question("What is the capital of France?", "Paris", ["Paris", "London", "Berlin", "Rome"])
    # generate random choices for each question
    question2 = Question("What is the capital of Germany?", "Berlin", ["Rome", "Oslo", "Berlin", "Paris"])
    question3 = Question("What is the capital of Spain?", "Madrid", ["Madrid", "Paris", "Berlin", "Rome"])
    question4 = Question("What is the capital of Italy?", "Rome", ["Rome", "London", "Berlin", "Paris"])
    question5 = Question("What is the capital of Poland?", "Warsaw", ["Warsaw", "London", "Berlin", "Rome"])
    question6 = Question("What is the capital of Sweden?", "Stockholm", ["Stockholm", "London", "Berlin", "Rome"])
    question7 = Question("What is the capital of Norway?", "Oslo")
    question8 = Question("What is the capital of Denmark?", "Copenhagen", ["Copenhagen", "London", "Berlin", "Rome"])
    question9 = Question("What is the capital of Finland?", "Helsinki", ["Helsinki", "London", "Berlin", "Rome"])
    question10 = Question("What is the capital of Iceland?", "Reykjavik", ["Reykjavik", "London", "Berlin", "Rome"])
    quiz = Quiz([question1, question2, question3, question4, question5, question6, question7, question8, question9, question10])
    return quiz 