class Question:
    def __init__(self, query: str, answer: str):
        self.query = query
        self.answer = answer

    def __str__(self):
        return self.query