import os


class RabbitmqBroker:
    address = os.getenv('RABBITMQ_HOST', "amqp://guest:guest@localhost/")
    restaurant_data_queue = 'restaurant_data_notify'


class DBConstants:
    dataset_name = 'datacenter'
    table_name = 'restaurants'


class BucketConfig:
    Bucket_name = str(os.getenv('BUCKET_NAME', 'datacenter-analysis'))
