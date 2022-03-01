import googlemaps


class Google_API:
    def __init__(self, keyword):

        gmaps = googlemaps.Client(key="")
        self.geocode_result = gmaps.geocode(keyword)

    def get_coordinates(self):

        if self.geocode_result:
            lat = self.geocode_result[0]["geometry"]["location"]["lat"]
            lng = self.geocode_result[0]["geometry"]["location"]["lng"]
            print(self.geocode_result[0])
            return (lat, lng)
        else:
            return None