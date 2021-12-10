import os


class DBConstants:
    DB_address = str(os.getenv('DATABASE_URL', 'postgresql://postgres:admin@172.17.32.3:5432/restaurant_database'))
                                                            #user:password
    ES_adddress = str(os.getenv('ES_URL', 'http://10.108.13.19:9200'))


class BucketConfig:
    Bucket_name = str(os.getenv('BUCKET_NAME', 'datacenter-analysis'))
