class Interpretation:
    def __init__(self, category, explanation, source=None):
        self.category = category
        self.explanation = explanation
        self.source = source

    def __str__(self):
        return f"{self.category}: {self.explanation}"