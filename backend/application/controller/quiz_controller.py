from application.model import Quiz, Question
import random


def generate_quiz(content: list, generator) -> Quiz:

    generated_QA = []

    for paragraph in content:
        generated_QA.extend(generator.generateQA(paragraph))

    answers = [dic['answer'] for dic in generated_QA]

    # for dic in generated_QA:
    #     print(dic)

    # breakpoint()

    list_of_question_instances = [
        Question(dic['question'], dic['answer'], [dic['answer']] + random.choices(answers, k=3))
        for dic in generated_QA if 'question' in dic]

    return Quiz(list_of_question_instances)
