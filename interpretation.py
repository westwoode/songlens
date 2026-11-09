class Interpretation:
    def __init__(self, category, explanation, source=None):
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category must be a non-empty string.")

        if not isinstance(explanation, str) or not explanation.strip():
            raise ValueError("Explanation must be a non-empty string.")

        if source is not None and not isinstance(source, str):
            raise TypeError("Source must be a string or None.")

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

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["category"],
            data["explanation"],
            data.get("source")
        )