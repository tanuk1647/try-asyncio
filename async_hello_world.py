import asyncio
import sys

async def sleep_and_write(char, time=0):
    await asyncio.sleep(time)
    sys.stdout.write(char)
    return char

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop_was_not_running = not loop.is_running()
    def print_hello_world(future):
        print(''.join(future.result()))
        if loop_was_not_running:
            loop.stop()
    coroutines = (
        sleep_and_write("w", 0.8),
        sleep_and_write("l", 1.1),
        sleep_and_write("r", 1.0),
        sleep_and_write("o", 0.9),
        sleep_and_write("d", 1.2),
        sleep_and_write("l", 0.3),
        sleep_and_write("e", 0.1),
        sleep_and_write(",", 0.6),
        sleep_and_write("h"),
        sleep_and_write(" ", 0.7),
        sleep_and_write("o", 0.5),
        sleep_and_write("l", 0.2),
        sleep_and_write("\n", 1.3))
    future = asyncio.gather(*coroutines)
    asyncio.ensure_future(future)
    future.add_done_callback(print_hello_world)
    if loop_was_not_running:
        loop.run_forever()
