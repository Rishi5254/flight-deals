from data_manager import DataManager
from flight_IATA_Finder import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

dm = DataManager()
flight_code = FlightData()
flight_search = FlightSearch()
notification_manager = NotificationManager()


data = dm.get_data()
city_names = [n['city'] for n in data]
prices = [n['lowestPrice'] for n in data]
codes = flight_code.get_iata_code(city_names)
dm.put_data(codes)
least_list = flight_search.get_flight_details(codes)

for index, code in enumerate(codes):
    message = least_list[code]
    if least_list[code][0] <= prices[index]:
        notification_manager.send_message(message)

