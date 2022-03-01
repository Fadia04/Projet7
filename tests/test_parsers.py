import pytest
from classes.parsers import Parser

# from classes import parsers


class TestParser:
    QUESTION = "dis-moi où se trouve la Tour Montparnasse ?"

    def test_should_remove_upper_case(self):
        # question ="dis-moi où se trouve la Tour Montparnasse ?"
        # parseur = Parser(question)
        parseur = Parser(self.QUESTION)
        # question = "Peux-tu me Poser Une Question?"
        # assert parseur.remove_upper_case("Peux-tu me Poser Une Question?")== "peux-tu me poser une question?"
        # mess= parseur.remove_upper_case(question)
        # assert mess == "peux-tu me poser une question?"
        # assert parseur.remove_upper_case(question)== "peux-tu me poser une question?"
        parseur.remove_upper_case()
        assert parseur.question == "dis-moi où se trouve la tour montparnasse ?"

    # def test_should_remove_upper_case():
    # sut = Parser(QUESTION)
    # sentence = "Peux-tu Me Poser Une Question?"
    # expected_value = "peux-tu me poser une question?"
    # assert sut.remove_upper_case(sentence)== expected_value

    def test_should_parse(self):
        parseur = Parser(self.QUESTION)
        parseur.parse()
        assert parseur.question == "dismoi ou se trouve la tour montparnasse "

    def test_should_remove_ponctuation(self):
        parseur = Parser(self.QUESTION)
        parseur.remove_ponctuation()
        assert parseur.question == "dismoi où se trouve la Tour Montparnasse "

    def test_should_remove_accents(self):
        parseur = Parser(self.QUESTION)
        parseur.remove_accents()
        assert parseur.question == "dis-moi ou se trouve la Tour Montparnasse ?"

    def test_should_remove_unless_word(self):
        parseur = Parser(self.QUESTION)
        parseur.parse()

        assert parseur.keywords == ["tour", "montparnasse"]

    def test_should_get_keyword(self):
        parseur = Parser(self.QUESTION)
        parseur.parse()

        assert parseur.get_keyword() == "tour montparnasse"

    if __name__ == "__main__":
        pytest.main()
