import flask
import requests
import os
from flask import jsonify
from bitly import Bitly


app = flask.Flask(__name__)
app.config["DEBUG"] = True
bitly_object = Bitly()

@app.route('/', methods=['GET'])
def home():
    group = bitly_object.group_getter()
    bitlink = bitly_object.bitlink_getter(group)       
    data = bitly_object.clicks_getter(bitlink)
    print(data)
    #return data

if __name__ == "__main__":

    app.run()
