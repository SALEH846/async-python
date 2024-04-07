import asyncio


async def fetch_data(uid: int, sleep_time: int) -> dict:
    print(f"Coroutine {uid} starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"uid": uid, "sleep_time": sleep_time, "data": f"Sample data from coroutine {uid}"}


async def main() -> None:
    tasks = []
    # TaskGroup is better for error handling
    # It will cancel all the tasks automatically if one of them fails
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # After the task group block, all tasks have finished
    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")


asyncio.run(main())
