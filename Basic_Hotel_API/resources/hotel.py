from flask_restful import Resource

hotels = [
    {
        'hotel_id': 'alpha',
        'name': 'Alpha Hotel',
        'stars': 4.3,
        'rate': 420.41,
        'city': 'Los Angeles'
    },
    {
        'hotel_id': 'beta',
        'name': 'Beta Hotel',
        'stars': 5.0,
        'rate': 627.85,
        'city': 'Los Angeles'
    },
    {
        'hotel_id': 'omega',
        'name': 'Omega Hotel',
        'stars': 2.1,
        'rate': 190.52,
        'city': 'Villa Cubas'
    },
]

class Hotels(Resource):
    def get(self):
        return {'hotels': hotels}
    
class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id: return hotel
            return {'message': 'Hotel not found!'}, 404

    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass