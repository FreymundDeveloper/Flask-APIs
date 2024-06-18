from flask_restful import Resource, reqparse
from models.user import UserModel
    
class User(Resource):
    ## API Route Methods
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