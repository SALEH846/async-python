import asyncio


async def waiter(event: asyncio.Event) -> None:
    print("Waiting for the event to be set")
    await event.wait()
    print("Event has been set, continuing execution")


async def setter(event: asyncio.Event) -> None:
    await asyncio.sleep(2)
    event.set()
    print("Event has been set!")


async def main() -> None:
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))


asyncio.run(main())