import asyncio


# Coroutine that simulates a time-consuming task
async def fetch_data(delay: int, uid: int) -> dict:
    print("Fetching Data...", uid)
    await asyncio.sleep(delay)  # Simulate an I/O operation with a sleep
    print("Data Fetched...", uid)
    return {"data": "Some data...", "uid": uid}


async def main() -> None:
    # ----------------------
    # # The following will behave like synchronous code
    # # A coroutine only starts executing when we await it, not when we call it
    # task1 = fetch_data(2, 1)
    # task2 = fetch_data(2, 2)
    #
    # # Here, `task1` will start executing
    # result1 = await task1
    # print(f"Received result: {result1}")
    #
    # # Now, `task2` will start executing after `task1` has finished
    # result2 = await task2
    # print(f"Received result: {result2}")
    # ----------------------

    # Create tasks for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data(2, 2))
    task2 = asyncio.create_task(fetch_data(3, 3))
    task3 = asyncio.create_task(fetch_data(1, 1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

    # ----------------------

asyncio.run(main())
