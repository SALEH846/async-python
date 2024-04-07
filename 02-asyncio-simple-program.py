import asyncio


# Coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching Data...")
    await asyncio.sleep(delay)  # Simulate an I/O operation with a sleep
    print("Data Fetched...")
    return {"data": "Some data..."}


async def main():
    print("Start of main coroutine")
    task = fetch_data(2)
    # await the `fetch_data` coroutine, pausing execution of main until `fetch_data` completes
    result = await task
    print(f"Received result: {result}")
    print("End of main coroutine")

# NOTE: A coroutine only starts executing when we await it, not when we call it

asyncio.run(main())
