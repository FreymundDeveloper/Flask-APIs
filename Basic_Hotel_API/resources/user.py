from flask_restful import Resource, reqparse
from models.user import UserModel
    
class User(Resource):
    ## API Route Methods (/users)
    def get(self, user_id):
        user = UserModel.find_user(user_id)

        if user: return user.json()
        return {'message': 'User not found!'}, 404

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
                return { 'message': 'User deleted!' }
            except:
                return { 'message': 'An internal error ocurred trying to delete data.'}, 500
            
        return { 'message': 'User not found!' }, 404
    
class UserReagister(Resource):
    ## API Route Methods (/register)
    def post(self):
        arguments = reqparse.RequestParser()
        arguments.add_argument('login', type=str, required=True, help="This field (login) is required.")
        arguments.add_argument('password', type=str, required=True, help="This field (password) is required.")

        data = arguments.parse_args()

        if UserModel.find_by_login(data['login']):
            return { 'message': 'The login ({}) already exists.'.format(data['login']) }
        
        user = UserModel(**data)
        user.save_user()
        return { 'message': 'User created successfully!' }, 201
        