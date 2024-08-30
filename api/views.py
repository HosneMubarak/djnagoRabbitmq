from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import send_message_to_queue


@api_view(['POST'])
def send_message(request):
    message = request.data.get('message', 'Test Message')
    send_message_to_queue(message)
    return Response({"status": "Message sent to RabbitMQ", "message": message})
