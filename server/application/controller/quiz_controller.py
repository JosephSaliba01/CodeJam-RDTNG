from application.model import Quiz, Question

def generate_quiz(content: str):
    question1 = Question("What is the capital of France?", "Paris")
    question2 = Question("What is the capital of Germany?", "Berlin")
    question3 = Question("What is the capital of Spain?", "Madrid")
    question4 = Question("What is the capital of Italy?", "Rome")
    question5 = Question("What is the capital of Poland?", "Warsaw")
    question6 = Question("What is the capital of Sweden?", "Stockholm")
    question7 = Question("What is the capital of Norway?", "Oslo")
    question8 = Question("What is the capital of Denmark?", "Copenhagen")
    question9 = Question("What is the capital of Finland?", "Helsinki")
    question10 = Question("What is the capital of Iceland?", "Reykjavik")
    quiz = Quiz([question1, question2, question3, question4, question5, question6, question7, question8, question9, question10])
    return quiz 