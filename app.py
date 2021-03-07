import flask
from flask import jsonify, request
import json
from bitly import Bitly
from helper import Helper


app = flask.Flask(__name__)
app.config["DEBUG"] = True

bitly_object = Bitly()
helper_object = Helper()

@app.route('/', methods=['GET'])
def home():
    dir(request)
    # Get default user group
    group = bitly_object.group_getter() 
    # Get the links for the user default group
    group_links = bitly_object.bitlink_getter(group['default_group_guid'])
    # Return identifying bitlink along with its countries click data
    links = helper_object.json_snippet_builder(group_links)
    # generate 30 day avg from country click data and build dict
    data = helper_object.avg_calculator(links)
    
    return jsonify(data)

if __name__ == "__main__":

    app.run()
