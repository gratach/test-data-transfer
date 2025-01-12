import asyncio

async def test():
    print('test')
    await asyncio.sleep(1)
    print('test2')

async def main():
    task = asyncio.create_task(test())
    print("The task is running")
    await asyncio.sleep(3)
    print("Now we wait for the task to finish")
    await task
    print("The task is done")

asyncio.run(main())