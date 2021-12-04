from models import db
from google.cloud import bigquery
from google.api_core.exceptions import Conflict
from config import DBConstants


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
        print("Created dataset {}.{}".format(db.project, dataset.dataset_id))
    except Conflict as e:
        print(e)
    # [END bigquery_create_dataset]


def create_table(table_name):

    # table_id = "your-project.your_dataset.your_table_name"
    try:
        table_id = db.project + '.' + DBConstants.dataset_name + '.' + table_name
        schema = [
            bigquery.SchemaField("alias", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("rating", "FLOAT64", mode="REQUIRED"),
            bigquery.SchemaField("price", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("phone", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("distance", "FLOAT64", mode="REQUIRED"),
            bigquery.SchemaField("zip_code", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("city", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("state", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("address", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("review_count", "NUMERIC", mode="REQUIRED"),
            bigquery.SchemaField("categories", "STRING", mode="REPEATED"),
        ]

        table = bigquery.Table(table_id, schema=schema)
        table = db.create_table(table)  # Make an API request.
        print(
            "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
        )
    except Conflict as e:
        print(e)