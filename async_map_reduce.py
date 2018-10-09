import asyncio
import concurrent.futures
from datetime import datetime

async def sum_(start, stop):
    print('{}, start[{}-{}]'.format(datetime.now(), start, stop))
    loop = asyncio.get_event_loop()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        x = await loop.run_in_executor(executor, sum, range(start, stop))
    print('{}, end[{}-{}]'.format(datetime.now(), start, stop))
    return x

def async_sum():
    print('{}, async_sum start'.format(datetime.now()))
    loop = asyncio.get_event_loop()
    loop_was_not_running = not loop.is_running()
    def reduce(future):
        print(sum(future.result()))
        if loop_was_not_running:
            loop.stop()
        print('{}, async_sum end'.format(datetime.now()))
    coroutines = (
        sum_(0, 250000000),
        sum_(250000000, 500000000),
        sum_(500000000, 750000000),
        sum_(750000000, 1000000000))
    future = asyncio.gather(*coroutines)
    asyncio.ensure_future(future)
    future.add_done_callback(reduce)
    if loop_was_not_running:
        loop.run_forever()

def normal_sum():
    print('{}, normal_sum start'.format(datetime.now()))
    print(sum(range(0, 1000000000)))
    print('{}, normal_sum end'.format(datetime.now()))

if __name__ == '__main__':
    normal_sum()
    async_sum()
