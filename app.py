import flask
from flask import jsonify
from bitly import Bitly
from helper import Helper


app = flask.Flask(__name__)
app.config["DEBUG"] = True

bitly_object = Bitly()
helper_object = Helper()

@app.route('/', methods=['GET'])
def home():
    # Get default user group
    group = bitly_object.group_getter() 
    # Get the links for the users group
    group_links = bitly_object.bitlink_getter(group['default_group_guid'])
    
    links = helper_object.json_snippet_builder(group_links)
    
    data = helper_object.avg_calculator(links)

    print(data)
if __name__ == "__main__":

    app.run()
