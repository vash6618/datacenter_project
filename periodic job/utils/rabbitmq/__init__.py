from aio_pika import connect, Message
from config import RabbitmqBroker

connection = None


async def connect_broker(loop):
    # Perform connection
    global connection
    connection = await connect(RabbitmqBroker.address, loop=loop)
    print(connection)


async def send_message(message):
    global connection
    # Creating a channel
    channel = await connection.channel()


    # Sending the message
    await channel.default_exchange.publish(
        routing_key=RabbitmqBroker.restaurant_data_notify_queue,
        message=Message(body=message)
    )

    print(" [x] Sent message for analysis")


async def close_conn_broker():
    global connection
    await connection.close()

