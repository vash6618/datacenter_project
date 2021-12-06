from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch('http://localhost:9200')
# docs = [
#         {
#             "id": "SFlAWPKHOJEsTttBLUj8Hw",
#             "alias": "mountain-sun-pub-and-brewery-boulder",
#             "name": "Mountain Sun Pub & Brewery",
#             "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/mdNeb6dQzmqvPRrTCX6ovw/o.jpg",
#             "is_closed": False,
#             "url": "https://www.yelp.com/biz/mountain-sun-pub-and-brewery-boulder?adjust_creative=KTfBfdeA9Wmq5JoDcIt_mQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=KTfBfdeA9Wmq5JoDcIt_mQ",
#             "review_count": 1492,
#             "categories": [
#                 {
#                     "alias": "pubs",
#                     "title": "Pubs"
#                 },
#                 {
#                     "alias": "burgers",
#                     "title": "Burgers"
#                 },
#                 {
#                     "alias": "breweries",
#                     "title": "Breweries"
#                 }
#             ],
#             "rating": 4.5,
#             "coordinates": {
#                 "latitude": 40.01916,
#                 "longitude": -105.2753
#             },
#             "transactions": [
#                 "delivery"
#             ],
#             "price": "$$",
#             "location": {
#                 "address1": "1535 Pearl St",
#                 "address2": "",
#                 "address3": "",
#                 "city": "Boulder",
#                 "zip_code": "80302",
#                 "country": "US",
#                 "state": "CO",
#                 "display_address": [
#                     "1535 Pearl St",
#                     "Boulder, CO 80302"
#                 ]
#             },
#             "phone": "+13035460886",
#             "display_phone": "(303) 546-0886",
#             "distance": 2693.0322782379153
#         },
#         {
#             "id": "1LMe5UqMS2ei_ubt46FbNA",
#             "alias": "the-buff-restaurant-boulder",
#             "name": "The Buff Restaurant",
#             "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/YYwTOALz94UUxaY6XcTGdA/o.jpg",
#             "is_closed": False,
#             "url": "https://www.yelp.com/biz/the-buff-restaurant-boulder?adjust_creative=KTfBfdeA9Wmq5JoDcIt_mQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=KTfBfdeA9Wmq5JoDcIt_mQ",
#             "review_count": 1535,
#             "categories": [
#                 {
#                     "alias": "breakfast_brunch",
#                     "title": "Breakfast & Brunch"
#                 },
#                 {
#                     "alias": "salad",
#                     "title": "Salad"
#                 },
#                 {
#                     "alias": "soup",
#                     "title": "Soup"
#                 }
#             ],
#             "rating": 4.5,
#             "coordinates": {
#                 "latitude": 40.017245,
#                 "longitude": -105.2602784
#             },
#             "transactions": [
#                 "delivery"
#             ],
#             "price": "$$",
#             "location": {
#                 "address1": "2600 Canyon Blvd",
#                 "address2": "",
#                 "address3": "",
#                 "city": "Boulder",
#                 "zip_code": "80302",
#                 "country": "US",
#                 "state": "CO",
#                 "display_address": [
#                     "2600 Canyon Blvd",
#                     "Boulder, CO 80302"
#                 ]
#             },
#             "phone": "+13034429150",
#             "display_phone": "(303) 442-9150",
#             "distance": 1918.2074131587112
#         },
#         {
#             "id": "FJo2jznp56MU_IdDcX038A",
#             "alias": "avery-brewing-boulder-2",
#             "name": "Avery Brewing",
#             "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/qW5o3UunzGRu2l7vTE2oPw/o.jpg",
#             "is_closed": False,
#             "url": "https://www.yelp.com/biz/avery-brewing-boulder-2?adjust_creative=KTfBfdeA9Wmq5JoDcIt_mQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=KTfBfdeA9Wmq5JoDcIt_mQ",
#             "review_count": 1001,
#             "categories": [
#                 {
#                     "alias": "breweries",
#                     "title": "Breweries"
#                 },
#                 {
#                     "alias": "bbq",
#                     "title": "Barbeque"
#                 },
#                 {
#                     "alias": "tradamerican",
#                     "title": "American (Traditional)"
#                 }
#             ],
#             "rating": 4.5,
#             "coordinates": {
#                 "latitude": 40.062575,
#                 "longitude": -105.204776
#             },
#             "transactions": [
#                 "delivery"
#             ],
#             "price": "$$",
#             "location": {
#                 "address1": "4910 Nautilus Ct N",
#                 "address2": "",
#                 "address3": "",
#                 "city": "Boulder",
#                 "zip_code": "80301",
#                 "country": "US",
#                 "state": "CO",
#                 "display_address": [
#                     "4910 Nautilus Ct N",
#                     "Boulder, CO 80301"
#                 ]
#             },
#             "phone": "+13034404324",
#             "display_phone": "(303) 440-4324",
#             "distance": 5049.40569470092
#         }
#     ]
# doc = {
#     'alias': 'mountain-sun-pub-and-brewery-boulder',
#     'name': 'Mountain Sun Pub & Brewery',
#     'categories': [{
#                     "alias": "pubs",
#                     "title": "Pubs"
#                 },
#                 {
#                     "alias": "burgers",
#                     "title": "Burgers"
#                 },
#                 {
#                     "alias": "breweries",
#                     "title": "Breweries"
#                 }],
#     "rating": 4.5,
#     "price": "$$",
#     'timestamp': datetime.now(),
# }
# for doc in docs:
#     resp = es.index(index="restaurants", document=doc)
#     print(resp['result'])


# resp = es.get(index="test-index", id=1)P
# print(resp['_source'])


resp = es.search(index="restaurants", query={"query_string": {'query': 'breweries'}})
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print(hit['_source'])


# es.indices.delete(index='restaurants')



