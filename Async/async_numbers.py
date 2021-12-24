import asyncio


async def find_divisible(inrange, divby):
    print(inrange, ' ', divby)
    located = []
    for i in range(inrange):
        if i % divby == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.0001)
    print(inrange, ' ', divby)
    return located


async def main():
    div1 = loop.create_task(find_divisible(508000, 34113))
    div2 = loop.create_task(find_divisible(100052, 3210))
    div3 = loop.create_task(find_divisible(500, 3))
    await asyncio.wait([div1, div2, div3])
    return div1, div2, div3

if __name__ == '__main__':
    # create a loop
    try:
        loop = asyncio.get_event_loop()
        d1, d2, d3 = loop.run_until_complete(main())
        # get results
        print(d1.result())
        print(d2.result())
        print(d3.result())
    except Exception as e:
        pass
    finally:
        # close the loop
        loop.close()
