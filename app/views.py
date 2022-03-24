import aiohttp_jinja2
import aiohttp.web as web
import service
from config import SRV
import json


@aiohttp_jinja2.template("mainpage.jinja2")
async def mainpage(request):
    return {'SRV': SRV}


async def start_button(request):
    return web.json_response(await service.start())


async def stop_button(request):
    return web.json_response(await service.stop())


async def restart_button(request):
    return web.json_response(await service.restart())


async def status_button(request):
    return web.json_response(await service.status())


async def checkbox_status(request):
    return web.json_response({'checkbox': await service.checkbox()})


async def checkbox_save(request):
    await service.checkbox_save(request.rel_url.query['checkbox'])
    return web.json_response('ok')
