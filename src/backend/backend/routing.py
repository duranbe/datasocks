#mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from .middleware import WebSocketAuthMiddleware
import datasocks.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': WebSocketAuthMiddleware(
        URLRouter(
            datasocks.routing.websocket_urlpatterns
        )
    ),
})