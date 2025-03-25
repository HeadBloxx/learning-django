import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack  # For handling authentication

from chat.routing import websocket_urlpatterns  # Import your WebSocket URLs

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP handling
    "websocket": AuthMiddlewareStack(  # This ensures the WebSocket connection is routed correctly
        URLRouter(websocket_urlpatterns)
    ),  
})
