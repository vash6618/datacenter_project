from models import db
from google.cloud import bigquery
import logging
from google.api_core.exceptions import Conflict
from config import DBConstants

logging.basicConfig(format="%(message)s")
logging.root.setLevel(logging.INFO)


def create_dataset(dataset_name):
    # dataset = bigquery.Dataset(dataset_id)
    try:
        dataset_ref = bigquery.DatasetReference.from_string(dataset_name, default_project=db.project)
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = 'US'
        # Send the dataset to the API for creation, with an explicit timeout.
        # Raises google.api_core.exceptions.Conflict if the Dataset already
        # exists within the project.
        dataset = db.create_dataset(dataset, timeout=30)  # Make an API request.
        logging.info("Created dataset {}.{}".format(db.project, dataset.dataset_id))
    except Conflict as e:
        logging.info(e)
    # [END bigquery_create_dataset]


def create_table(table_name):

    # table_id = "your-project.your_dataset.your_table_name"
    try:
        table_id = db.project + '.' + DBConstants.dataset_name + '.' + table_name
        schema = [
            bigquery.SchemaField("alias", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("name", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("rating", "FLOAT64", mode="NULLABLE"),
            bigquery.SchemaField("price", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("phone", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("distance", "FLOAT64", mode="NULLABLE"),
            bigquery.SchemaField("zip_code", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("city", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("state", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("address", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("review_count", "NUMERIC", mode="NULLABLE"),
            bigquery.SchemaField("categories", "STRING", mode="REPEATED"),
            bigquery.SchemaField("external_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("image_url", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("id", "NUMERIC", mode="NULLABLE")
        ]

        table = bigquery.Table(table_id, schema=schema)
        table = db.create_table(table)  # Make an API request.
        logging.info(
            "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
        )
    except Conflict as e:
        logging.info(e)