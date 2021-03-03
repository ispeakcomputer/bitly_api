import flask
import requests
import os


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Testing</h1>"



class Bitly:

    def __init__(self):
        self.bitly_token = os.environ.get('BITLYTOKEN')
    def group_getter(self):
        url = 'https://api-ssl.bitly.com/v4/user'
        try:
            response = requests.get(url, headers={'Authorization': 'Bearer ' + self.bitly_token})
            html = response.text
            if html:
                print(html) 
        except:
           print('error') 


if __name__ == "__main__":

    bitly_object = Bitly()
    bitly_object.group_getter
    app.run()
