from data_manager import DataManager
import requests
shetty_data = DataManager()

class CustomerAcquisition:
    def __init__(self):
        self.TOKEN = "GFkgg7T6798SADFgfdsa34sdfgv"
        self.END_POINT = "https://api.sheety.co/d783e6050e140daa5a547b9b942d0a8b/copyOfFlightDeals/users"
        self.PARAS = {
            "Authorization": f"Bearer {self.TOKEN}"
        }
    def user_inputs(self):
        print("Welcome to Flight Club.")
        print("We Find the Best flight deals and email you.")
        first_name = input("What is your first name?: ").title()
        last_name = input("What is your last name?: ").title()
        user_email = ""
        repeat = True
        while repeat:
            email = input("What is your email?: ").lower()
            verify_email = input("Type your email again").lower()
            if email == verify_email:
                user_email += email
                repeat = False
                print("WELCOME TO THE CLUB!")
            else:
                print("Email not matched\nEnter your email again")

        return [first_name, last_name, user_email]

    def get_data(self):
        response = requests.get(url=self.END_POINT, headers=self.PARAS)
        response.raise_for_status()
        data = response.json()
        return data

    def post_user_details(self):
        user_details = self.user_inputs()
        data = self.get_data()['users']
        print(len(data))
        if len(data) == 0:
            get_last_id = 2
        else:
            get_last_id = self.get_data()['users'][-1]['id'] + 1
        data = {
            "user": {
                "firstName": user_details[0],
                "lastName": user_details[1],
                "email": user_details[2],
                "id": get_last_id
            }
        }
        response = requests.post(url=self.END_POINT, headers=self.PARAS, json=data)
        response.raise_for_status()


user = CustomerAcquisition()
user.post_user_details()