import requests
import json
import datetime

class WodParser:
    def __init__(self, base_url, date_str_fmt):
        self.base_url = base_url
        self.date_str_fmt = date_str_fmt
    
    def get_url(self, date):
        date_str = datetime.datetime.strftime(date, self.date_str_fmt)
        return self.base_url.format(date_str)

    def get_wod(self, date):
        r = requests.get(self.get_url(date))
        return self.parse_wod(r.text)

    def parse_wod(self, response):
        htmlcont_loc = response.find("htmlContent")
        if htmlcont_loc == -1:
            print("didn't find htmlcontent in response")
            return -1
        end_loc = response.find("}", htmlcont_loc)
        wod_json = json.loads(response[htmlcont_loc - 2: end_loc + 1])
        return wod_json['htmlContent']