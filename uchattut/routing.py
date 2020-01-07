from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
import chat.routing
from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # (http->django views are added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
    'channel': ChannelNameRouter({
        'chat': ChatConsumer,
    }),
})
