import asyncio


# OLD
@asyncio.coroutine
def hello_old():
    while True:
        print("Hello")
        yield from asyncio.sleep(1.0)


# NEW
async def hello():
    while True:
        print("Hello")
        await asyncio.sleep(1.0)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(hello())
    # loop.close()
    asyncio.run(hello())