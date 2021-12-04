from google.cloud import bigquery
import logging
from google.oauth2 import service_account
logging.basicConfig(format="%(message)s")
logging.root.setLevel(logging.INFO)

db = None


async def connect_db():
    global db
    key_path = 'pod-key.json'
    db = bigquery.Client.from_service_account_json(key_path)
    logging.info(db)