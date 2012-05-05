import requests
import json

def geocode(address):
    params = dict(format='json', q=address, email='eric@ericstein.org', limit=1)
    base_url = 'http://nominatim.openstreetmap.org/search'
    r = requests.request('GET', url=base_url, params=params)
    data = r.text
    parsed = json.loads(data)[0]
    return (parsed['display_name'], (parsed['lat'], parsed['lon']),)

if __name__ == '__main__':
    print geocode(19078)
