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
    group = bitly_object.group_getter() 
    if 'FORBIDDEN' in group.values():
        return jsonify({'message':'Bitly token is bad, broken or expired.'})
    else:
        group_links = bitly_object.bitlink_getter(group['default_group_guid'])
        links = helper_object.json_snippet_builder(group_links)
        data = helper_object.avg_calculator(links)
        
        return jsonify(data)

if __name__ == "__main__":
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
        group = bitly_object.group_getter() 
        
        if 'FORBIDDEN' in group.values():
            print('\033[31m' + ' * Error: Bitly doesn\'t like your token. Replace or check it. Exiting.')
            print('\033[39m')
        else:
            app.run(host="0.0.0.0")
