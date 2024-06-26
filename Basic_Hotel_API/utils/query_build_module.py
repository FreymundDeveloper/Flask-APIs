from models.hotel import HotelModel

## -> Hotel Model Content

## Default "/hotels" Params Values
def normalize_path_params(city = None, stars_min = 0, stars_max = 5, rate_min = 0, 
                          rate_max = 10000, limit = 50, offset = 0):
    if city: 
        return {
            'stars_min': stars_min, 'stars_max': stars_max,
            'rate_min': rate_min, 'rate_max': rate_max,
            'city': city,
            'limit': limit, 'offset': offset,
        }
    
    return {
        'stars_min': stars_min, 'stars_max': stars_max,
        'rate_min': rate_min, 'rate_max': rate_max,
        'limit': limit, 'offset': offset,
    }

## SQL Query for Hotels Table
def hotel_query_build(params):
    if params.get('city', ''):
        search_result = (HotelModel.query
                        .filter(HotelModel.city == params['city'])
                        .filter(HotelModel.stars >= params['stars_min'], HotelModel.stars <= params['stars_max'])
                        .filter(HotelModel.rate >= params['rate_min'], HotelModel.rate <= params['rate_max'])
                        .order_by(HotelModel.stars.desc())
                        .offset(params['offset']).limit(params['limit'])
                        .all())
    else:
        search_result = (HotelModel.query
                        .filter(HotelModel.stars >= params['stars_min'], HotelModel.stars <= params['stars_max'])
                        .filter(HotelModel.rate >= params['rate_min'], HotelModel.rate <= params['rate_max'])
                        .order_by(HotelModel.stars.desc())
                        .offset(params['offset']).limit(params['limit'])
                        .all())
        
    return search_result

## -> User Model Content
## -> Website Model Content