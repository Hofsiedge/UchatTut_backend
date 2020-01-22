# from    channels.auth       import AuthMiddlewareStack
from    channels.routing    import ProtocolTypeRouter, URLRouter, ChannelNameRouter
import  events.routing
from    events.consumers    import EventConsumer

from events.middleware import TokenAuthMiddlewareStack

application = ProtocolTypeRouter({
    # (http->django views are added by default)
    'websocket': TokenAuthMiddlewareStack(
        URLRouter(
            events.routing.websocket_urlpatterns
        )
    ),
    'channel': ChannelNameRouter({
        'events': EventConsumer,
    }),
})
