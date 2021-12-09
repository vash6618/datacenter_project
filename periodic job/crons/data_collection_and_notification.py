import logging, requests
from config import YELP_API, get_api_offset, set_api_offset, DBConstants
from urllib.parse import quote
from models.restaurants import Restaurants
from models import db, es
from utils.rabbitmq import send_message
import pickle
logging.basicConfig(format="%(message)s")
logging.root.setLevel(logging.INFO)


async def yelp_request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def get_restaurant_categories(categories):
    final_list = []
    if categories:
        for category in categories:
            final_list.append(category['title'])
    return final_list


async def fetch_data_and_notify() -> None:
    """
    fetches restaurant data from yelp and pushes it to a message queue
    """
    url_params = {
        'location': YELP_API.DEFAULT_LOCATION,
        'limit': YELP_API.LIMIT,
        'offset': get_api_offset()
    }

    restaurants = await yelp_request(host=YELP_API.API_HOST, path=YELP_API.SEARCH_PATH, api_key=YELP_API.API_KEY,
                                     url_params=url_params)
    restaurants = restaurants[YELP_API.SEARCH_API_OBJECTS]

    # for now extracting only the name and alias of the restaurants
    db_restaurant_objects = [{'name': restaurant.get('name'), 'alias': restaurant.get('alias'), 'external_id': restaurant.get('id'),
                              'image_url': restaurant.get('image_url'), 'review_count': restaurant.get('review_count'),
                              'rating': restaurant.get('rating'), 'address': restaurant.get('location').get('display_address')[0],
                              'phone': restaurant.get('phone'), 'categories':
                                  get_restaurant_categories(restaurant.get('categories')), 'price': restaurant.get('price'),
                              'city': restaurant.get('location').get('city'), 'distance': restaurant.get('distance'),
                              'zip_code': restaurant.get('location').get('zip_code'),
                              'state': restaurant.get('location').get('state')
    }
                             for restaurant in restaurants]

    set_api_offset()
    async with db.transaction():
        values = await Restaurants.insert().values(db_restaurant_objects).returning(Restaurants.id).gino.all()
        for i in range(len(db_restaurant_objects)):
            restaurant = db_restaurant_objects[i]
            restaurant['id'] = values[i].id
            resp = es.index(index=DBConstants.ES_index_name, document=restaurant)
        byte_message = pickle.dumps(db_restaurant_objects)
        await send_message(byte_message)



