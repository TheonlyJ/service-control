import aiohttp_jinja2


@aiohttp_jinja2.template("mainpage.jinja2")
async def mainpage(request):
    print('wtf')
    return {'active': None,
            'error': 'Something is wrong'}
