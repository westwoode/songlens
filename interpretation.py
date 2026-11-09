class Interpretation:
    def __init__(self, category, explanation, source=None):
        self.category = category
        self.explanation = explanation
        self.source = source

    def __str__(self):
        return f"{self.category}: {self.explanation}"

    def to_dict(self):
        return {
            "category": self.category,
            "explanation": self.explanation,
            "source": self.source
        }