import re
import unidecode
from classes.stopwords import stopwords


QUESTION = "dis-moi où se trouve à là Toùr Montparnassé ?"

class Parser:
    def __init__(self, question):
        self.question = question
        self.keywords = []
        

    def parse(self):
        self.remove_upper_case()
        self.remove_ponctuation()
        self.remove_accents()
        self.remove_unless_word()

    def remove_unless_word(self):
        for word in self.question.split():
            if word not in stopwords:
                self.keywords.append(word)

    def remove_upper_case(self):
        self.question =  self.question.lower()

    def remove_ponctuation(self):
        self.question = re.sub(r'[^\w\s]','',self.question)


    def remove_accents(self):
        self.question = unidecode.unidecode(self.question)

    def get_keyword(self):
        if len(self.keywords) != 0:
            return (" ").join(self.keywords)
        return None

"""
if __name__ == '__main__':
    parser = Parser(QUESTION)
    parser.parse()
    print(parser.get_keyword())"""


