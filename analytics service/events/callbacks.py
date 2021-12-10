from aio_pika import IncomingMessage
import logging, pickle
import matplotlib.pyplot as plt
from config import DBConstants, BucketConfig
from google.cloud import storage
from google.oauth2 import service_account
# from matplotlib.backends import backend_pdf
import logging
logging.basicConfig(format="%(message)s")
logging.root.setLevel(logging.INFO)



def plot_graph_ratings(x_values, x_ticks, y_values, x_label, y_label, title, save_format):
    '''plot a bar graph'''
    plt.figure()
    plt.bar(x=x_values, height=y_values)
    plt.ylim(0, 400)
    plt.xticks(x_values, x_ticks)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # plt.title(title)
    plt.savefig(save_format)


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
    key_path = 'pod-key.json'
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    client = storage.Client(credentials=credentials, project=credentials.project_id)
    bucket = client.get_bucket(BucketConfig.Bucket_name)
    logging.info(bucket)
    for i in range(4):
        object_name_in_gcs_bucket = bucket.blob('/srv/restaurants_vs_price_{}.png'.format(i+1))
        object_name_in_gcs_bucket.upload_from_filename('/srv/restaurants_vs_price_{}.png'.format(i+1))
        object_name_in_gcs_bucket = bucket.blob('/srv/price_vs_restaurants_{}.png'.format(i + 1))
        object_name_in_gcs_bucket.upload_from_filename('/srv/price_vs_restaurants_{}.png'.format(i + 1))


def perform_analysis(query):
    from models import db
    query_job = db.query(query)  # Make an API request.
    cnt = 0
    for row in query_job:
        # Row values can be accessed by field name or index.
        cnt = row["restaurants"]
    return cnt


def analytics(table_name):
    from models import db
    table_id = db.project + '.' + DBConstants.dataset_name + '.' + table_name
    prices = ['$', '$$', '$$$', '$$$$']
    for i in range(1, 5):
        cnt = []
        for price in prices:
            query = """
                    SELECT COUNT(name) as restaurants FROM {} where price='{}' and rating >= {}
                """.format(table_id, price, i)
            cnt.append(perform_analysis(query))
        print(cnt)
        x_values = [1,2,3,4]
        y_values = cnt
        plot_graph_ratings(x_values, ['$', '$\$', '$\$\$', '$\$\$\$'], y_values, 'price', 'restaurants',
                           '', 'restaurants_vs_price_{}.png'.format(i))
    ind = 1
    for price in prices:
        cnt = []
        for i in range(1, 5):
            query = """
                    SELECT COUNT(name) as restaurants FROM {} where price='{}' and rating >= {} and rating <= {}
                """.format(table_id, price, i, i+1)
            cnt.append(perform_analysis(query))
        print(cnt)
        x_values = [1,2,3,4]
        y_values = cnt
        plot_graph_ratings(x_values, ['1-2', '2-3', '3-4', '4-5'], y_values, 'restaurant ratings', 'restaurants',
                           '', 'price_vs_restaurants_{}.png'.format(ind))
        ind += 1







def table_insert_rows(table_name, message):
    from models import db
    # table_id = "your-project.your_dataset.your_table"
    table_id = db.project + '.' + DBConstants.dataset_name + '.' + table_name
    rows_to_insert = message

    errors = db.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        logging.info("New rows have been added.")
    else:
        logging.info("Encountered errors while inserting rows: {}".format(errors))


async def consume_restaurant_data(message: IncomingMessage):
    logging.info('Inserting data')
    message_body = pickle.loads(message.body)
    table_insert_rows(DBConstants.table_name, message_body)
    analytics(DBConstants.table_name)
    # upload_file()

    # print(message_body)
    # tuples = await db.status(db.text("select rating, review_count from restaurants"))
    # rating_reviews = tuples[1]
    # freq_ratings = defaultdict(int)
    # freq_reviews = defaultdict(int)

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
    # #
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
