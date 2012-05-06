import requests
import json

class AddressNotFound(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

def geocode(address):
    params = dict(format='json', q=address, email='eric@ericstein.org', limit=1)
    base_url = 'http://nominatim.openstreetmap.org/search'
    r = requests.request('GET', url=base_url, params=params)
    data = r.text
    try:
        parsed = json.loads(data)[0]
    except IndexError:
        raise AddressNotFound("Address not found.")
    return (parsed['display_name'], (parsed['lat'], parsed['lon']),)

