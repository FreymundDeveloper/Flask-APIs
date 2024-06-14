from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hotels(Resource):
    def get(self):
        return {'hotels': 'my hotels'}
    
api.add_resource(Hotels, '/hotels')

if __name__ == '__main__':
    app.run(debug=True)