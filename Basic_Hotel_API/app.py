from flask import Flask
from flask_restful import Api

from resources.hotel import Hotels

app = Flask(__name__)
api = Api(app)
    
api.add_resource(Hotels, '/hotels')

if __name__ == '__main__':
    app.run(debug=True)