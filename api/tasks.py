import pika
from django.conf import settings


def send_message_to_queue(message):
    """
      Sends a message to a RabbitMQ queue.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=pika.PlainCredentials(
                username=settings.RABBITMQ_USERNAME,
                password=settings.RABBITMQ_PASSWORD
            )
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue=settings.RABBITMQ_QUEUE_NAME)

    # Sending a simple message to RabbitMQ
    channel.basic_publish(
        exchange='',
        routing_key=settings.RABBITMQ_QUEUE_NAME,
        body=message
    )
    print(f"Sent message: {message}")
    connection.close()
