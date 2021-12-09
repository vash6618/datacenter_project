offset = 0
import os


class YELP_API:
    API_HOST = 'https://api.yelp.com'
    SEARCH_PATH = '/v3/businesses/search'
    BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
    API_KEY = 'S5yeWO6fxZhmOfZuOr01TL7Tz7NHFD2cZwwVxj4--WiN6dEttgmZJsvnPSM9YMfDT0Cadx91cKK99bRiLWcgCO9AVTgpIjsJj3NHTGSuL3s1TYZY0XU2IamjdFKjYXYx'
    DEFAULT_LOCATION = 'Boulder, CO'
    LIMIT = 10
    SEARCH_API_OBJECTS = 'businesses'


class DBConstants:
    DB_address = str(os.getenv('DATABASE_URL', 'postgresql://postgres:admin@10.42.96.3:5432/restaurant_database'))
    # DB_address = str(os.getenv('DATABASE_URL', 'postgresql://postgres:admin@34.132.60.82:5432/restaurant_database'))
    #user:password
    ES_adddress = str(os.getenv('ES_URL', 'http://10.28.9.96:9200'))
    # ES_adddress = str(os.getenv('ES_URL', 'http://localhost:9200'))
    ES_index_name = 'restaurants'


class RabbitmqBroker:
    address = os.getenv('RABBITMQ_HOST', "amqp://guest:guest@localhost/")
    restaurant_data_notify_queue = 'restaurant_data_notify'


class CRON_INTERVAL:
    fetch_data_and_notify = 40


def set_api_offset():
    global offset
    offset += YELP_API.LIMIT

def get_api_offset():
    return offset