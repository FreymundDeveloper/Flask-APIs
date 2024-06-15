from flask_restful import Resource, reqparse
from models.hotel import HotelModel

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
    ## API Routes 
    def get(self):
        return {'hotels': hotels}
    
class Hotel(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('name')
    arguments.add_argument('stars', type=float)
    arguments.add_argument('rate', type=float)
    arguments.add_argument('city')

    ## API Routes 
    def get(self, hotel_id):
            hotel = HotelModel.find_hotel(hotel_id)

            if hotel: return hotel.json()
            return {'message': 'Hotel not found!'}, 404

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id): return { 'messege': 'Hotel id ({}) already exists!'.format(hotel_id) }, 400

        data = Hotel.arguments.parse_args()
        hotel = HotelModel(hotel_id, **data)
        hotel.save_hotel()

        return hotel.json(), 201

    def put(self, hotel_id):
        data = Hotel.arguments.parse_args()
        hotel_found = HotelModel.find_hotel(hotel_id)

        if hotel_found: 
            hotel_found.update_hotel(**data)
            hotel_found.save_hotel()
            return hotel_found.json(), 200
        
        hotel = HotelModel(hotel_id, **data)
        hotel.save_hotel()
        return hotel.json(), 201

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            hotel.delete_hotel()
            return { 'message': 'Hotel deleted!' }
        return { 'message': 'Hotel not found!' }, 404