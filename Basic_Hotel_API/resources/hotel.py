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