import wikipedia


class Wiki_API:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_data(self):
        wikipedia.set_lang("fr")
        geosearch = wikipedia.geosearch(self.latitude, self.longitude)
        if geosearch:
            page_title = geosearch[0]

            if page_title:
                self.link = wikipedia.page(page_title)
                url = self.link.url
                summary = self.link.summary

                return (summary, url)
            else:
                return None
        else:
            return None


