import requests
import json
import os

class Bitly:

    def __init__(self, token):
        self.token = token
        self.headers={'Authorization': 'Bearer ' + token}
        self.user_url = 'https://api-ssl.bitly.com/v4/user'
        self.bitlink_url='https://api-ssl.bitly.com/v4/groups/{}/bitlinks'
        self.clicks_url ='https://api-ssl.bitly.com/v4/bitlinks/{}/countries'
    
    def group_getter(self):
        try:
            response = requests.get(self.user_url, headers = self.headers)
            return json.loads(response.text) 
        except Exception as e:
            print(e)

    def bitlink_getter(self,group):
        full_bitlink_url = self.bitlink_url.format(group)
        try:
            response = requests.get( full_bitlink_url, headers = self.headers)
            return json.loads(response.text)
        except Exception as e:
            print(e) 

    def clicks_getter(self, bitlink):
        full_clicks_url = self.clicks_url.format(bitlink)
        try:
            response = requests.get( full_clicks_url, headers = self.headers)
            return json.loads(response.text)      
        except Exception as e:
            print(e) 
