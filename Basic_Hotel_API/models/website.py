from sql_alchemy import database

class WebsiteModel(database.Model):
    __tablename__ = 'websites'

    website_id = database.Column(database.Integer, primary_key=True)
    url = database.Column(database.String(80))
    hotels = database.relationship('HotelModel')

    def __init__(self, url):
        self.url = url

    def json(self):
        return {
            'website_id': self.website_id,
            'url': self.url,
            'hotels': [hotel.json() for hotel in self.hotels]
        }
    
    @classmethod
    def find_website(cls, url):
        website = cls.query.filter_by(url=url).first()

        if website: return website
        return None
    
    @classmethod
    def find_by_id(cls, website_id):
        website = cls.query.filter_by(website_id=website_id).first()

        if website: return website
        return None
    
    def save_website(self):
        database.session.add(self)
        database.session.commit()

    def delete_website(self):
        [hotel.delete_hotel() for hotel in self.hotels]

        database.session.delete(self)
        database.session.commit()