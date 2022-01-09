import requests

API_KEY = "e601db544bdc7845512adcb00e7b0339"
END_POINT = "http://api.exchangeratesapi.io/v1/latest"

class CurrencyExchange:

    def rupee_value(self):
        parameters = {
            "access_key": API_KEY,
        }
        response = requests.get(url=END_POINT, params=parameters)
        response.raise_for_status()
        data = response.json()['rates']['INR']
        return data

    def eur_to_inr(self, amount):
        value = self.rupee_value()
        return round(amount * value)

    def inr_to_eur(self, amount):
        value = self.rupee_value()
        return round(amount/value)





