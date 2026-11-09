class LyricLine:
    def __init__(self, text, line_number, interpretations=None):
        self.text = text
        self.line_number = line_number

        if interpretations is None:
            self.interpretations = []
        else:
            self.interpretations = interpretations

    def add_interpretation(self, interpretation):
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