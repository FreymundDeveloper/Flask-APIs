from flask_restful import Resource
from models.website import WebsiteModel

class Websites(Resource):
    def get(self):
        return {'websites': [website.json() for website in WebsiteModel.query.all()]}
    
class Website(Resource):
    def get(self, url):
        website = WebsiteModel.find_website(url)

        if website: return website.json()
        return { 'message': 'Website not found!'}, 404
    
    def post(self, url):
        if WebsiteModel.find_website(url):
            return { 'message': 'The website ({}) already exists!'.format(url)}, 400
        
        website = WebsiteModel(url)

        try: 
            website.save_website()
        except:
            return { 'message': 'An internal error ocurred trying to save data.'}, 500
        
        return website.json()

    def delete(self, url):
        website = WebsiteModel.find_website(url)

        if website:
            website.delete_website()
            return { 'message': 'Website deleted!'}
        return { 'message': 'Website not found!'}, 404