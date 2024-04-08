import time
from aiohttp import web
from SAFARI.route import routes


StartTime = time.time()
__version__ = 1.1


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
