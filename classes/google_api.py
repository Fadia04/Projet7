import googlemaps



class Google_API:
    def __init__(self, keyword):
        
        gmaps= googlemaps.Client(key='AIzaSyA65eDiflrrmBjvWlCPKqlta9W0tBqKs-I')
        self.geocode_result = gmaps.geocode(keyword)
        
                   
    def get_coordinates(self):
        
        if self.geocode_result: 
            #return (self.geocode_result[0]["geometry"]["location"])
            #address = self.geocode_result[0]["formatted_address"]
            lat = self.geocode_result[0]["geometry"]["location"]["lat"]
            lng = self.geocode_result[0]["geometry"]["location"]["lng"]
            return (lat, lng)
        else:
            return None 
"""
a = Google_API('paris pantheon')
a.get_coordinates()
print(a.get_coordinates())"""
