from django.urls import path
from .views import send_message

urlpatterns = [
    path('api/send-message/', send_message, name='send_message'),
]
