import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from utils.create_manual_psql import create_database_psql
from config_mail import ConfigMail
from blacklist import BLACKLIST
from resources.hotel import Hotels, Hotel
from resources.user import User, UserReagister, UserLogin, UserLogout, UserConfirm
from resources.website import Websites, Website
from utils.mail_builder import mail

## App configs

load_dotenv()

app = Flask(__name__)

## SQLite DB Option
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskapis.db'

## PostgreSQL DB Option
## app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('USER')}:{os.getenv('PASSWORD')}@{os.getenv('LOCALHOST')}:{os.getenv('PORT')}/{os.getenv('DATABASE')}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_BLACKLIST_ENABLED'] = True

## Mailtrap Configs

app.config.from_object(ConfigMail)
mail.init_app(app)

## Cors Config

CORS(app)

api = Api(app)
jwt = JWTManager(app)

## API Routes

api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<string:hotel_id>')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserReagister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(Websites, '/websites')
api.add_resource(Website, '/websites/<string:url>')
api.add_resource(UserConfirm, '/confirmation/<int:user_id>')

## Token Validates

@jwt.token_in_blocklist_loader
def verify_blacklist(self,token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def access_token_invalid(jwt_header, jwt_payload):
    return jsonify({ 'message': 'You have been logged out!'}), 401

## App running

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)

    ## Call create psql database
    ## create_database_psql()

    with app.app_context():
        database.create_all()
    app.run(debug=True)