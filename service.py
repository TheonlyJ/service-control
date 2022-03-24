import asyncio
from config import SRV
import re


async def command(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()
    return stdout.decode(), stderr.decode()


async def action(act):
    await command(f'systemctl {act} {SRV}')
    stdout, stderr = await command(f'systemctl status {SRV}')
    return stdout, stderr


async def start():
    stdout, stderr = await action('start')
    active = re.search(r'(Active: active \(running\).*;)', stdout)
    if active:
        return {'result': active.group(0)}
    else:
        return {'error': f'Service did not start:\n {stderr}'}


async def stop():
    stdout, stderr = await action('stop')
    active = re.search(r'(Active: inactive \(dead\).*;)', stdout)
    if active:
        return {'result': active.group(0)}
    else:
        return {'error': f'Service did not stop:\n {stderr}'}


async def restart():
    stdout, stderr = await action('restart')
    active = re.search(r'(Active: active \(running\).*;)', stdout)
    if active:
        return {'result': active.group(0)}
    else:
        return {'error': f'Service did not restart:\n {stderr}'}


async def status():
    stdout, stderr = await command(f'systemctl status {SRV}')
    active = re.search(r'(Active:.*;)', stdout)
    if active:
        return {'result': active.group(0)}
    else:
        return {'error': f'Service did not return status:\n {stderr}'}


