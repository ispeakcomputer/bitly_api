import flask
import os
from flask import jsonify, request
import json
from bitly import Bitly
from helper import Helper
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

jwt_username = os.environ.get('JWTUSER')
jwt_password = os.environ.get('JWTPASS')
jwt_secret_key  = os.environ.get('JWT_SECRET_KEY')
token = os.environ.get('BITLYTOKEN')

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JWT_SECRET_KEY"] = jwt_secret_key  # Change this!

bitly_object = Bitly(token)
helper_object = Helper(token)

# Create a route to authenticate your users and return JWTs.
jwt = JWTManager(app)
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != jwt_username or password != jwt_password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/', methods=['GET'])
@jwt_required()
def home():
    # Get default user group
    group = bitly_object.group_getter() 
    # Sends user the message that Bitly doesnt like their token.
    if 'FORBIDDEN' in group.values():
        return jsonify({'message':'Bitly token is bad, broken or expired.'})
    else:
        # Get the links for the user default group
        group_links = bitly_object.bitlink_getter(group['default_group_guid'])
        # Return identifying bitlink along with its countries click data
        links = helper_object.json_snippet_builder(group_links)
        # generate 30 day avg from country click data and build dict
        data = helper_object.avg_calculator(links)
        
        return jsonify(data)

if __name__ == "__main__":
    #Checks settings and reports warnings or kills app if the Bitly Token is gone or not valid
    if jwt_username and jwt_password == "test":
        print('\033[33m' + ' * WARNING: Jwt username and password are default. Change this for production.')
        print('\033[39m')

    if jwt_secret_key == "changethis" :
        print('\033[33m' + ' * WARNING: Jwt Secret is set to default. Change this for production.')
        print('\033[39m')
    if not token:
        print('\033[31m' + ' * Error: Bitly API token missing. Exiting.')
        print('\033[39m')
        quit() 
    else:
        #Check our token exists and that Bitly likes it before starting
        group = bitly_object.group_getter() 
        
        if 'FORBIDDEN' in group.values():
            print('\033[31m' + ' * Error: Bitly doesn\'t like your token. Replace or check it. Exiting.')
            print('\033[39m')
        else:
            # app.run(host="0.0.0.0", port=80)
            app.run(host="0.0.0.0")
