import googlemaps

import os


class Google_API:
    def __init__(self, keyword):
        google_api_key = os.getenv("GOOGLE_SECRET_KEY")
        gmaps = googlemaps.Client(key=google_api_key)
        self.geocode_result = gmaps.geocode(keyword)

    def get_coordinates(self):

        if self.geocode_result:
            lat = self.geocode_result[0]["geometry"]["location"]["lat"]
            lng = self.geocode_result[0]["geometry"]["location"]["lng"]
            print(self.geocode_result[0])
            return (lat, lng)
        else:
            return None