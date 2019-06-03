# -*- coding: utf-8 -*-
import logging;logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web

# routes = web.RouteTableDef()


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


# @routes.get('/')
async def index(request):
    return web.Response(text='hello')


def init():
    app = web.Application()
    app.router.add_routes([web.get('/', index)])
    logging.info('服务启动在：http://127.0.0.1:8080')
    web.run_app(app, host='127.0.0.1', port=8080)


init()
