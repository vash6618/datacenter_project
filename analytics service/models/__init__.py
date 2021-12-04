from google.cloud import bigquery
# pylint: disable=invalid-name
# Connect to the database
db = None


async def connect_db():
    global db
    db = bigquery.Client()
    print(db)