import requests
import os

class Bitly:

    def __init__(self):
        self.headers={'Authorization': 'Bearer ' + os.environ.get('BITLYTOKEN')}
        self.user_url = 'https://api-ssl.bitly.com/v4/user'
        self.bitlink_url='https://api-ssl.bitly.com/v4/groups/{}/bitlinks'
        self.clicks_url ='https://api-ssl.bitly.com/v4/bitlinks/{}/countries'
    
    def group_getter(self):
        try:
            response = requests.get(self.user_url, headers = self.headers)
            if response.json
                return response.json 
        except:
           print('error') 
    def bitlink_getter(self,group):
        full_bitlink_url = self.bitlink_url.format(group)
        try:
            response = requests.get( full_bitlink_url, headers = self.headers)
            html = response.text
            if html:
                print(html) 
        except:
           print('error') 

    def clicks_getter(self, bitlink):
        full_clicks_url = self.clicks_url.format(bitlink)
        try:
            response = requests.get( full_clicks_url, headers = self.headers)
            html = response.text
            if html:
                print(html) 
        except:
           print('error') 
