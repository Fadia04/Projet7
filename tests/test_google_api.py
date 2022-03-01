from pickle import NONE
import pytest
from classes.google_api import Google_API


class MockResponseOk:
    @staticmethod
    def geocode(keyword):
        result = [{"geometry": {"location": {"lat": 1200, "lng": 3000}}}]
        return result


class MockResponseNok:
    @staticmethod
    def geocode(keyword):
        result = []
        return result


class TestGoogleAPI:
    def mock_get_ok(*args, **kwargs):
        return MockResponseOk()

    def mock_get_nok(*args, **kwargs):
        return MockResponseNok()

    def test_should_get_coordinates(self, monkeypatch):
        monkeypatch.setattr("googlemaps.Client", self.mock_get_ok)
        gapi = Google_API("Tour Eiffel Paris")
        assert gapi.get_coordinates() == (1200, 3000)

    def test_should_not_get_coordinates(self, monkeypatch):
        monkeypatch.setattr("googlemaps.Client", self.mock_get_nok)
        gapi = Google_API("Tour Eiffel Paris")
        assert gapi.get_coordinates() == None
