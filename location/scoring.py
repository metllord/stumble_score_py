import requests
from geocode import geocode
import json

requests.defaults.defaults['encode_uri'] = False

class StumbleScore:
    def __init__(self, address):
        self.location = geocode(address)
        self.params = dict(
            key = 'AIzaSyAehiOU6RPqcSc_sWh1e6gl8CSfOmi0EaM',
            type = 'bar|liquor_store|night_club',
            location = '%s,%s' % self.location[1],
            radius = 2000,
            sensor = 'false')
        self.url = 'https://maps.googleapis.com/maps/api/place/search/json'

    def search(self):
        page = requests.request('GET', url=self.url, params=self.params)
        data = page.text
        self.parsed =  json.loads(data)

    def bar_count(self):
        return len(self.parsed)

    def score(self):
        return self.bar_count() * 5.0

    def category(self):
        score = self.score()
        if score >= 100:
            return 'Sloppy'
        elif score >= 50:
            return 'Tippsy'
        else:
            return 'Dry'


