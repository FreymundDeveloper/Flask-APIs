from sql_alchemy import database

class HotelModel(database.Model):
    __tablename__ = 'hotels'

    hotel_id = database.Column(database.String, primary_key=True)
    name = database.Column(database.String(80))
    stars = database.Column(database.Float(precision=1))
    rate = database.Column(database.Float(precision=2))
    city = database.Column(database.String(40))


    def __init__(self, hotel_id, name, stars, rate, city):
        self.hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.rate = rate
        self.city = city

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'stars': self.stars,
            'rate': self.rate,
            'city': self.city
        }
    
    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()

        if hotel: return hotel
        return None
    
    def save_hotel(self):
        database.session.add(self)
        database.session.commit()

    def update_hotel(self, name, stars, rate, city):
        self.name = name
        self.stars = stars
        self.rate = rate
        self.city = city