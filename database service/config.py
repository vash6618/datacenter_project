import os


class DBConstants:
    DB_address = str(os.getenv('DATABASE_URL', 'postgresql://postgres:admin@10.42.96.3:5432/restaurant_database'))
                                                            #user:password
    ES_adddress = str(os.getenv('ES_URL', 'http://10.28.9.96:9200'))


class BucketConfig:
    Bucket_name = str(os.getenv('BUCKET_NAME', 'datacenter-analytics'))
