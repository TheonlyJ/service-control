import aiohttp_jinja2
import aiohttp.web as web
from service import *
from config import SRV
import json


@aiohttp_jinja2.template("mainpage.jinja2")
async def mainpage(request):
    return {'SRV': SRV}


async def start_button(request):
    print('start called')
    return web.json_response(await start())


async def stop_button(request):
    print('stop called')
    return web.json_response(await stop())


async def restart_button(request):
    print('restart called')
    return web.json_response(await restart())


async def status_button(request):
    print('status called')
    return web.json_response(await status())
