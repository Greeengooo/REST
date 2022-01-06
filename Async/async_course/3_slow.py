import asyncio


async def sleep_task(n):
    for i in range(5):
        print(f"task {n} iter: {i}")
        await asyncio.sleep(1)
    return n


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task_list = [loop.create_task(sleep_task(n)) for n in range(3)]
    rsp = loop.run_until_complete(asyncio.gather(*task_list))
    loop.close()
    print(rsp)
