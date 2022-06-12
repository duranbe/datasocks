#mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from .middleware import TokenAuthMiddleware
import datasocks.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': TokenAuthMiddleware(
        URLRouter(
            datasocks.routing.websocket_urlpatterns
        )
    ),
})