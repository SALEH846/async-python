import  asyncio
from asyncio import Future


async def set_future_result(future: Future, value: str) -> None:
    await asyncio.sleep(2)

    # set the result of the future
    future.set_result(value)

    print(f"Set the future's result to: {value}")


async def main() -> None:
    # Create a future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    # Schedule setting the future's result
    asyncio.create_task(set_future_result(future, "Future result is empty"))

    # Wait for the future's result
    result = await future
    print(f"Received the future's result: {result}")


asyncio.run(main())