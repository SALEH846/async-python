import asyncio


async def fetch_data(uid: int, sleep_time: int) -> dict:
    print(f"Coroutine {uid} starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"uid": uid, "data": f"Sample data from coroutine {uid}", "sleep_time": sleep_time}


async def main():
    # Run coroutines concurrently and gather their values
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))

    # `gather` method is not good for error handling as if one of the coroutines fail, it will not
    # cancel the other ones automatically

    # Process the results
    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())
