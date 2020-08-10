import asyncio
import date_and_time

def ams_cron():
    x = range(0,60,5)
    return x

def na_cron():
    x = range(0,60,10)
    return x

async def ams_collection():
    print("                      hello from AMS")


async def na_collection():
    await asyncio.sleep(20)
    print('                      hello from NA')

async def schedular():
    second = 61
    while (1):
        last_second = second
        print('second = ' + str(second))
        if second in na_cron():
            asyncio.create_task(na_collection())
        if second in ams_cron():
            asyncio.create_task(ams_collection())
        while (last_second == second):
            second = date_and_time.date_and_time.now().second
            pending = asyncio.all_tasks()
            print('    number of task(s) = ' + str(len(pending)))
            await asyncio.sleep(.3)

asyncio.run(schedular())
