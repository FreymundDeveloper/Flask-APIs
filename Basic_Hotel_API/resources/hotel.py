from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required

class Hotels(Resource):
    ## API Route Methods
    def get(self):
        return {'hotels': [hotel.json() for hotel in HotelModel.query.all()]}
    
class Hotel(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('name', type=str, required=True, help="This field (name) is required.")
    arguments.add_argument('stars', type=float)
    arguments.add_argument('rate', type=float, required=True, help="This field (rate) is required.")
    arguments.add_argument('city', type=str, required=True, help="This field (city) is required.")

    ## API Route Methods
    def get(self, hotel_id):
            hotel = HotelModel.find_hotel(hotel_id)

            if hotel: return hotel.json()
            return {'message': 'Hotel not found!'}, 404

    @jwt_required()
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id): return { 'messege': 'Hotel id ({}) already exists!'.format(hotel_id) }, 400

        data = Hotel.arguments.parse_args()
        hotel = HotelModel(hotel_id, **data)
        
        try:
            hotel.save_hotel()
            return hotel.json(), 201
        except:
            return { 'message': 'An internal error ocurred trying to save data.'}, 500

    @jwt_required()
    def put(self, hotel_id):
        data = Hotel.arguments.parse_args()
        hotel_found = HotelModel.find_hotel(hotel_id)

        if hotel_found: 
            try:
                hotel_found.update_hotel(**data)
                hotel_found.save_hotel()
                return hotel_found.json(), 200
            except:
                return { 'message': 'An internal error ocurred trying to update data.'}, 500
        
        hotel = HotelModel(hotel_id, **data)

        try:
            hotel.save_hotel()
            return hotel.json(), 201
        except:
            return { 'message': 'An internal error ocurred trying to save data.'}, 500

    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
                return { 'message': 'Hotel deleted!' }
            except:
                return { 'message': 'An internal error ocurred trying to delete data.'}, 500
            
        return { 'message': 'Hotel not found!' }, 404