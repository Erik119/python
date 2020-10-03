import asyncio
import random

def coro(arg):
    print(arg)

ips=[1,2,3,4,5,6,7,8,9,'einde']

async def do(a):
    print('>', a)
    await asyncio.sleep(random.uniform(1, 3))
    print('<', a)
    return a


tasks = asyncio.gather(*[do(x) for x in ips])
print(tasks)

loop = asyncio.get_event_loop()
result = loop.run_until_complete(tasks)
loop.close()


print(result)




