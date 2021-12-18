import wikipedia


class Wiki_API:
    
    def __init__(self, latitude, longitude):       
        self.latitude = latitude
        self.longitude = longitude
        

    def get_data(self):
        wikipedia.set_lang('fr')
        page_title = wikipedia.geosearch(self.latitude, self.longitude)[0]
        
        if page_title:
            self.link = wikipedia.page(page_title)
            url = self.link.url
            summary = self.link.summary
        
            return (summary, url)
        else:
            return None
"""     
a = Wiki_API(48.85837009999999, 2.2944813)
print(a.get_data())"""