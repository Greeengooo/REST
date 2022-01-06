import asyncio


async def client(message):
    reader, writer = await asyncio.open_connection("localhost",
                                                   50001)
    print(f"send: {message}")
    writer.write(message.encode())
    writer.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    message = "hi!"
    loop.run_until_complete(client(message))
    loop.close()