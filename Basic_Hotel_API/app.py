from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.hotel import Hotels, Hotel
from resources.user import User, UserReagister, UserLogin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskapis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'ThisIsAKey'

api = Api(app)
jwt = JWTManager(app)
    
api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<string:hotel_id>')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserReagister, '/register')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    with app.app_context():
        database.create_all()
    app.run(debug=True)