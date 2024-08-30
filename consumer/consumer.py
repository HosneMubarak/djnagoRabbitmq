import pika
import time

# Reading environment variables from the Docker Compose environment
RABBITMQ_HOST = 'rabbitmq'
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'
RABBITMQ_QUEUE_NAME = 'message_processing_queue'


def connect_to_rabbitmq():
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=RABBITMQ_HOST,
                    port=RABBITMQ_PORT,
                    credentials=pika.PlainCredentials(
                        username=RABBITMQ_USERNAME,
                        password=RABBITMQ_PASSWORD
                    )
                )
            )
            return connection
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Connection failed, retrying in 5 seconds...: {e}")
            time.sleep(5)


def process_task(task_data):
    """
    A time-consuming task.
    """
    print(f"Processing task: {task_data}")
    time.sleep(30)
    print("Task completed.")


def callback(ch, method, properties, body):
    # Decode the message from RabbitMQ
    task_data = body.decode()
    print(f"Received message: {task_data}")

    # Call the processing function with the task data
    process_task(task_data)

    # Acknowledge that the message has been processed successfully
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = connect_to_rabbitmq()

channel = connection.channel()
channel.queue_declare(queue=RABBITMQ_QUEUE_NAME)
channel.basic_consume(queue=RABBITMQ_QUEUE_NAME, on_message_callback=callback, auto_ack=False)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
