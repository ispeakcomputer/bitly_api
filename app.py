import flask
from flask import jsonify, request
import json
from bitly import Bitly
from helper import Helper
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = flask.Flask(__name__)
app.config["DEBUG"] = True

bitly_object = Bitly()
helper_object = Helper()
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.


@app.route('/', methods=['GET'])
@jwt_required()
def home():
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
    # app.run(host="0.0.0.0", port=80)
    app.run(host="0.0.0.0")
