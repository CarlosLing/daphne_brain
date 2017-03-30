from channels.routing import route

from iFEED_API.consumers import ifeed_ws_message, ifeed_ws_connect, ifeed_ws_disconnect
from iFEED_API.consumers import server_ws_connect, server_ws_message, server_ws_disconnect

channel_routing = [
    route("websocket.receive", ifeed_ws_message, path=r"/ifeed/"),
    route("websocket.connect", ifeed_ws_connect, path=r"/ifeed/"),
    route("websocket.disconnect", ifeed_ws_disconnect, path=r"/ifeed/"),
    
    route("websocket.receive", server_ws_message, path=r"/server/"),
    route("websocket.connect", server_ws_connect, path=r"/server/"),
    route("websocket.disconnect", server_ws_disconnect, path=r"/server/"),
]