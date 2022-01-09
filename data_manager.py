import requests
class DataManager:
    def __init__(self):
        self.TOKEN = "GFkgg7T6798SADFgfdsa34sdfgv"
        self.END_POINT = "https://api.sheety.co/d783e6050e140daa5a547b9b942d0a8b/copyOfFlightDeals/prices"
        self.PARAS = {
            "Authorization": f"Bearer {self.TOKEN}"
        }
        self.data = {}
    def get_data(self):
        response = requests.get(url=self.END_POINT, headers=self.PARAS)
        response.raise_for_status()
        data = response.json()
        self.data = data['prices']
        return self.data

    def put_data(self, city_code):
        n = 0
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city_code[n]
                }
            }
            requests.put(
                url=f"{self.END_POINT}/{city['id']}",
                json=new_data,
                headers=self.PARAS
            )
            n += 1




