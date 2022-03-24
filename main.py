from aiohttp import web
import jinja2
import aiohttp_jinja2
from app.routes import setup


if __name__ == '__main__':
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("app/templates"))
    setup(app)
    web.run_app(app, port=80)
