from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from utils.query_build_module import normalize_path_params, hotel_query_build
from flask_jwt_extended import jwt_required

## Path Params
path_params = reqparse.RequestParser()
path_params.add_argument('city', type=str, location='args')
path_params.add_argument('stars_min', type=float, location='args')
path_params.add_argument('stars_max', type=float, location='args')
path_params.add_argument('rate_min', type=float, location='args')
path_params.add_argument('rate_max', type=float, location='args')
path_params.add_argument('limit', type=float, location='args')
path_params.add_argument('offset', type=float, location='args')

class Hotels(Resource):
    ## API Route Methods
    def get(self):
        data = path_params.parse_args()
        data_validate = {key: value for key, value in data.items() if value}
        params = normalize_path_params(**data_validate)
        search_result = hotel_query_build(params)

        return {'hotels': [hotel.json() for hotel in search_result]}
    
class Hotel(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('name', type=str, required=True, help="This field (name) is required.")
    arguments.add_argument('stars', type=float)
    arguments.add_argument('rate', type=float, required=True, help="This field (rate) is required.")
    arguments.add_argument('city', type=str, required=True, help="This field (city) is required.")
    arguments.add_argument('website_id', type=int, required=True, help="This field (website_id) is required.")

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