class Question:
    def __init__(self, query: str, answer: str, choices: list):
        self.query = query
        self.answer = answer
        self.choices = choices

    def __str__(self):
        return self.query