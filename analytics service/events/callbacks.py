from aio_pika import IncomingMessage
import boto3
import logging, pickle

from botocore.exceptions import ClientError
from config import BucketConfig
import matplotlib.pyplot as plt
from config import DBConstants, BucketConfig
from google.cloud import storage
from matplotlib.backends import backend_pdf


def plot_graph_ratings(x_values, y_values, x_label, y_label, title):
    '''plot a bar graph'''
    fig = plt.figure(1)
    plt.bar(x=x_values, height=y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    for index, value in enumerate(y_values):
        plt.text(x_values[index], value + 0.5, value)

    return fig


def plot_graph_reviews(x_values, y_values, x_label, y_label, title):
    '''plot a scatter graph'''
    fig = plt.figure()
    plt.scatter(x=x_values, y=y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    return fig


def upload_file():
    """Upload a file to an Cloud bucket
    """
    client = storage.Client()
    bucket = client.get_bucket(BucketConfig.Bucket_name)
    object_name_in_gcs_bucket = bucket.blob('test1.py')
    object_name_in_gcs_bucket.upload_from_filename('test1.py')


def perform_analysis(table_name):
    from models import db
    table_id = db.project + '.' + DBConstants.dataset_name + '.' + table_name
    query = """
            SELECT COUNT(name) as total_cnt FROM {}
        """.format(table_id)
    query_job = db.query(query)  # Make an API request.

    print("The query data:")
    for row in query_job:
        # Row values can be accessed by field name or index.
        print("total-cnt {}".format(row["total_cnt"]))


def table_insert_rows(table_name, message):
    from models import db
    table_id = db.project + '.' + DBConstants.dataset_name + '.' + table_name

    # TODO(developer): Set table_id to the ID of table to append to.
    # table_id = "your-project.your_dataset.your_table"
    rows_to_insert = [message]

    errors = db.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))


async def consume_restaurant_data(message: IncomingMessage):
    message_body = pickle.loads(message.body)
    # table_insert_rows(DBConstants.table_name, message_body)
    perform_analysis(DBConstants.table_name)
    upload_file()

    # print(message_body)
    # tuples = await db.status(db.text("select rating, review_count from restaurants"))
    # rating_reviews = tuples[1]
    # freq_ratings = defaultdict(int)
    # freq_reviews = defaultdict(int)
    #
    # reviews = []
    # # freq_reviews = {}
    # for rating_review in rating_reviews:
    #     # ratings.append(rating_review[0])
    #     freq_ratings[rating_review[0]] += 1
    #
    # x_values = list(freq_ratings.keys())
    # x_values.sort()
    # y_values = [freq_ratings[val] for val in x_values]
    # print(freq_ratings)
    # rating_reviews.sort()
    #
    # fig1 = plot_graph_ratings([str(x_value) for x_value in x_values], y_values, 'ratings', 'number of restaurants',
    #                           'rating vs restaurant_count')
    # fig2 = plot_graph_reviews([val[0] for val in rating_reviews], [val[1] for val in rating_reviews], 'ratings',
    #                           'reviews count',
    #                           'rating vs reviews count')
    #
    # try:
    #     import os
    #     os.remove(S3Config.analytics)
    # except Exception:
    #     print("file_not_present")
    #
    # pdf = backend_pdf.PdfPages(S3Config.analytics)
    # pdf.savefig(fig1)
    # pdf.savefig(fig2)
    # pdf.close()
    # upload_file(S3Config.analytics)
    # import os
    # os.remove(S3Config.analytics)
