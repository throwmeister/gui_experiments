import asyncio

async def take_input():
    x = input('Hello: ')
    return x

async def count():
    print("One")
    await asyncio.create_task(take_input())
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")