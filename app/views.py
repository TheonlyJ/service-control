import aiohttp_jinja2
from service import *


@aiohttp_jinja2.template("mainpage.jinja2")
async def mainpage(request):
    print('wtf')
    return await status()

@aiohttp_jinja2.template("mainpage.jinja2")
async def start_button(request):
    return await start()


@aiohttp_jinja2.template("mainpage.jinja2")
async def stop_button(request):
    return await stop()


@aiohttp_jinja2.template("mainpage.jinja2")
async def restart_button(request):
    return await restart()
