from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/general/$', lambda ws, *args, **kwargs: logger.info(f"WebSocket connection received on {ws}")),
    re_path(r'ws/general/$', ChatConsumer.as_asgi()),
]
