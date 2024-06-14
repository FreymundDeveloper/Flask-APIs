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

    ## Methods
    def find_hotel(hotel_id):
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id: return hotel
        return None

    ## API Routes 
    def get(self, hotel_id):
            hotel = Hotel.find_hotel(hotel_id)

            if hotel: return hotel
            return {'message': 'Hotel not found!'}, 404

    def post(self, hotel_id):
        data = Hotel.arguments.parse_args()
        obj_hotel = HotelModel(hotel_id, **data)
        new_hotel = obj_hotel.json()

        hotels.append(new_hotel)
        return new_hotel, 201

    def put(self, hotel_id):
        data = Hotel.arguments.parse_args()
        obj_hotel = HotelModel(hotel_id, **data)
        new_hotel = obj_hotel.json()

        hotel = Hotel.find_hotel(hotel_id)

        if hotel: 
            hotel.update(new_hotel)
            return new_hotel, 200
        
        hotels.append(new_hotel)
        return new_hotel, 201

    def delete(self, hotel_id):
        global hotels
        hotels = [hotel for hotel in hotels if hotel['hotel_id'] != hotel_id]
        return { 'message': 'Hotel deleted!' }