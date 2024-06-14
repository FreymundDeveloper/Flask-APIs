class HotelModel:
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