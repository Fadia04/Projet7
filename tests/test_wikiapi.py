import pytest
from classes.wikiapi import Wiki_API
from classes.google_api import Google_API
from classes.wikiapi import Wiki_API
import wikipedia

"""   
class MockResponseOk:
    @staticmethod
    def geosearch(latitude, longitude):
        result =['Esplanade des Ouvriers-de-la-Tour-Eiffel',"L'esplanade des Ouvriers-de-la-Tour-Eiffel est une voie située dans le 7e arrondissement de Paris, en France." 
        ,'https://fr.wikipedia.org/wiki/Esplanade_des_Ouvriers-de-la-Tour-Eiffel']
        return result"""


class MockPage:
    def __init__(self, summary, url):
        self.url = url
        self.summary = summary


class Test_WikiAPI:
    def mock_geosearch_ok(*args, **kwargs):
        result = [
            "Montparnasse Rive Gauche",
            "Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse.",
            "https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche",
        ]
        return result

    def mock_geosearch_nok(*args, **kwargs):
        result = []
        return result

    def mock_page_ok(*args, **kwargs):
        page = MockPage(
            "Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse.",
            "https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche",
        )
        return page

    def test_should_get_data(self, monkeypatch):
        wikiapi = Wiki_API(0, 0)
        monkeypatch.setattr("wikipedia.geosearch", self.mock_geosearch_ok)
        monkeypatch.setattr("wikipedia.page", self.mock_page_ok)
        assert wikiapi.get_data() == (
            "Montparnasse Rive Gauche  est un centre commercial français situé dans le quartier Necker du 15e arrondissement de Paris. Situé au pied de la tour Montparnasse, il fait partie de l'Ensemble Immobilier Tour Maine-Montparnasse. Il accueillait notamment les Galeries Lafayette Montparnasse.",
            "https://fr.wikipedia.org/wiki/Montparnasse_Rive_Gauche",
        )

    def test_should_not_get_data(self, monkeypatch):
        wikiapi = Wiki_API(0, 0)
        monkeypatch.setattr("wikipedia.geosearch", self.mock_geosearch_nok)
        assert wikiapi.get_data() == None

    def mock_page_title_nok(*args, **kwargs):
        result = [""]
        return result

    def test_should_not_get_data_with_page_title_nok(self, monkeypatch):
        wikiapi = Wiki_API(0, 0)
        monkeypatch.setattr("wikipedia.geosearch", self.mock_page_title_nok)
        assert wikiapi.get_data() == None
