from twilio.rest import Client

class NotificationManager:
    def send_message(self, msg):
        account_sid = 'ACb6e24d33a95f3116e3a8ae96afc7e971'
        auth_token = 'e4fd5b9ce4c6738534a295f57f749f86'
        client = Client(account_sid, auth_token)
        msg = client.messages.create(
            body=f'🔥Lowest Price Alert!🔥\nOnly ₹{msg[0]} to Fly From {msg[2]} to {msg[3]} with {msg[1]-1} Stops on {msg[4]}',
            from_='+19283994204',
            to='+918143222173'
        )
        print(msg.sid)

