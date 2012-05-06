import requests
from geocode import geocode
import json

requests.defaults.defaults['encode_uri'] = False

class StumbleScore:
    def __init__(self, address):
        self.location = geocode(address)
        self.params = dict(
            key = 'AIzaSyAehiOU6RPqcSc_sWh1e6gl8CSfOmi0EaM',
            types = 'bar|liquor_store|night_club',
            location = '%s,%s' % self.location[1],
            radius = 3219,
            sensor = 'false')
        self.url = 'https://maps.googleapis.com/maps/api/place/search/json'

    def search(self):
        page = requests.request('GET', url=self.url, params=self.params)
        data = page.text
        self.parsed =  json.loads(data)

    def bar_count(self):
        return len(self.parsed['results'])

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

    def list_bars(self):
        return [x['name'] for x in self.parsed['results']]

    def __call__(self):
        self.search()
        results = dict(name=self.location[0], bar_count=self.bar_count(), score=self.score(), 
                    category=self.category(), locations=self.list_bars())
        return results
