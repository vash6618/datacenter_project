from gino import Gino
from config import DBConstants
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import RequestError
import logging, asyncio
logging.basicConfig(format="%(message)s")
logging.root.setLevel(logging.INFO)
# pylint: disable=invalid-name
# Connect to the database
db, es = None, None

async def connect_db():
    import ssl

    ctx = ssl.create_default_context(cafile="")
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    global db, es
    es = Elasticsearch(DBConstants.ES_adddress)
    try:
        es.indices.delete(index=DBConstants.ES_index_name)
    except Exception as e:
        logging.info(e)
    await asyncio.sleep(10)
    try:
        es.indices.create(index=DBConstants.ES_index_name)
    except RequestError as e:
        logging.info(e)
    db = Gino()
    await db.set_bind(DBConstants.DB_address, echo=True)
    print(db)