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