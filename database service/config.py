import os


class DBConstants:
    DB_address = str(os.getenv('DATABASE_URL', 'postgresql://postgres:admin@10.42.96.3:5432/restaurant_database'))
                                                            #user:password


class BucketConfig:
    Bucket_name = str(os.getenv('BUCKET_NAME', 'datacenter-analytics'))
