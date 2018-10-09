import asyncio

async def sleep_and_append(e, sorted_values):
    await asyncio.sleep(e)
    sorted_values.append(e)

def sleep_sort(array):
    loop = asyncio.get_event_loop()
    loop_was_not_running = not loop.is_running()
    sorted_values = []
    def print_sorted_values(future):
        print(sorted_values)
        if loop_was_not_running:
            loop.stop()
    coroutines = (sleep_and_append(e, sorted_values) for e in array)
    future = asyncio.gather(*coroutines)
    asyncio.ensure_future(future)
    future.add_done_callback(print_sorted_values)
    if loop_was_not_running:
        loop.run_forever()

if __name__ == '__main__':
    array = [5, 3, 6, 3, 6, 3, 1, 4, 7]
    sleep_sort(array)
