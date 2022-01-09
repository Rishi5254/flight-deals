import datetime as dt
import requests
from currencyexchanger import CurrencyExchange
curency_exchage = CurrencyExchange()

SEARCH_DAYS = 50

class FlightSearch:
    def __init__(self):
        self.END_POINT ="https://tequila-api.kiwi.com/v2/search"
        self.API_KEY = "uf2LYptFCSY7PBjKPNCmujLsm7eYytCo"

    def get_flight_details(self, city_codes):
        result = {}
        for city_code in city_codes:
            headers = {
                "apikey": self.API_KEY
            }
            parameters = {
                "fly_from": "HYD",
                "fly_to": city_code,
                "date_from": self.today_date(),
                "date_to": self.month_after_date(),
                "flight_type": "oneway",
                "partner_market": "ind",
                "locale": "in",
                "limit": 1
            }
            response = requests.get(url=self.END_POINT, params=parameters, headers=headers)
            response.raise_for_status()
            data = response.json()['data']

            price = curency_exchage.eur_to_inr(data[0]['price'])
            total_flights = len(data[0]['route'])
            starts_city = f"{data[0]['cityFrom']}-{data[0]['cityCodeFrom']}"
            destination_city = f"{data[0]['cityTo']}-{data[0]['cityCodeTo']}"
            date = data[0]['local_arrival'].split("T")[0]
            result[city_code] = [price, total_flights, starts_city, destination_city, date]

        return result

    def today_date(self):
        today = dt.datetime.now().date()
        date = today.strftime("%d/%m/%G")
        return date

    def month_after_date(self):
        date = dt.datetime.now().date() + dt.timedelta(days=SEARCH_DAYS)
        return date.strftime("%d/%m/%G")