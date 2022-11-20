import json


class Quiz:
    def __init__(self, questions: list):
        self.questions = questions

    def __repr__(self):
        return f"Quiz(questions={self.questions})"

    def __str__(self):
        return f"Quiz(iquestions={self.questions})"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
