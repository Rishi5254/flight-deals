
import requests

class FlightData:
    def __init__(self):
        self.API_KEY ="uf2LYptFCSY7PBjKPNCmujLsm7eYytCo"
        self.END_POINT = "https://tequila-api.kiwi.com/locations/query"
        self.headers = {
            "apikey": self.API_KEY,
        }

    def get_iata_code(self, city_name):
        codes = []
        for n in range(0, len(city_name)):
            parameters = {
                "term": city_name[n],
                "location_types": "city"
            }
            response = requests.get(url=self.END_POINT, params=parameters, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            code = data['locations'][0]['code']
            if code == None:
                inde = 0
                repeat = True
                while repeat:
                    code = data['locations'][inde]['code']
                    if code != None and 'india' in data['locations'][inde]['slug']:
                        repeat = False
                    inde += 1
            codes.append(code)
        return codes



