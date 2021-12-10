import pika, os, pickle
import sys

rabbitMQHost = os.getenv("RABBITMQ_HOST") or "localhost"

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbitMQHost))
channel = connection.channel()

# channel.exchange_declare(exchange='', exchange_type='fanout')

data = [{
            "alias": "mountain-sun-pub-and-brewery-boulder",
            "name": "Mountain Sun Pub & Brewery",
            "review_count": 1492,
            "categories": ["pubs","burgers","breweries"],
            "rating": 4.5,
            "price": "$$",
            "city": "Boulder",
            "zip_code": "80302",
            "address": "1535 Pearl St",
            "state": "CO",
            "phone": "+13035460886",
            "distance": 2693.0322782379153,
            "external_id": "1LMe5UqMS2ei_ubt46FbNA"
        }]
channel.basic_publish(exchange='', routing_key='test_notify', body=pickle.dumps(data))
print('published')
connection.close()
