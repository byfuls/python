#-*- coding: utf-8 -*-
import asyncio
import itertools
import sys

#@asyncio.coroutine
#def spin(msg):
async def spin(msg):
    print('[spin] start')
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            #yield from asyncio.sleep(.1)
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            print('[spin] CancelledError event occur')
            break
    write(' ' * len(status) + '\x08' * len(status))

#@asyncio.coroutine
#def slow_function():
async def slow_function():
    print('[slow_function] start')
    # 입출력을 위해 장시간 기다리는 것처럼 보이게 만든다
    #yield from asyncio.sleep(3)
    await asyncio.sleep(3)
    return 42

#@asyncio.coroutine
#def supervisor():
async def supervisor():
    #spinner = asyncio.async(spin('thinking!'))
    spinner = asyncio.create_task(spin('thinking!'))
    print('spinner object:', spinner)
    #result = yield from slow_function()
    print('[supervisor] 1')
    result = await slow_function()
    print('[supervisor] 2')
    spinner.cancel()
    print('[supervisor] 3')
    return result

def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('answer:', result)

if __name__ == '__main__':
    main()