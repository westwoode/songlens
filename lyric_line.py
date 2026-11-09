from interpretation import Interpretation

class LyricLine:
    def __init__(self, text, line_number, interpretations=None):
        self.text = text
        self.line_number = line_number

        if interpretations is None:
            interpretations = []

        if not isinstance(interpretations, list):
            raise TypeError("Interpretations must be a list.")

        if not all(
            isinstance(item, Interpretation)
            for item in interpretations
        ):
            raise TypeError("All interpretations must be Interpretation objects.")

        self.interpretations = interpretations

        if not isinstance(text, str) or not text.strip():
            raise ValueError("Lyric text must be a non-empty string.")

        if type(line_number) is not int or line_number < 1:
            raise ValueError("Line number must be a positive integer.")

    def add_interpretation(self, interpretation):
        if not isinstance(interpretation, Interpretation):
            raise TypeError("Only Interpretation objects can be added.")

        self.interpretations.append(interpretation)
    
    def __str__(self):
        return f"{self.line_number}. {self.text}"

    def to_dict(self):
        return {
            "text": self.text,
            "line_number": self.line_number,
            "interpretations": [
                interpretation.to_dict()
                for interpretation in self.interpretations
            ]
        }

    @classmethod
    def from_dict(cls, data):
        from interpretation import Interpretation

        interpretations = [
            Interpretation.from_dict(item)
            for item in data["interpretations"]
        ]

        return cls(
            data["text"],
            data["line_number"],
            interpretations
        )