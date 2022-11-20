from application.model import Quiz, Question
import random

def generate_quiz(content: list, generator) -> Quiz:
    
    generated_QA = []

    for paragraph in content:
        generated_QA.extend(generator.generateQA(paragraph))

    answers = [dic['answer'] for dic in generated_QA]

    list_of_question_instances = [
        Question(dic['question'], dic['answer'], [dic['answer']] + random.choices(answers, k=3))
        for dic in generated_QA]

    return Quiz(list_of_question_instances)
