import asyncio
from asyncio import Semaphore


async def access_resource(semaphore: Semaphore, resource_id) -> None:
    async with semaphore:
        # Simulate accessing a limited resource
        print(f"Accessing resource {resource_id}")
        await asyncio.sleep(1)
        print(f"Releasing resource {resource_id}")


async def main() -> None:
    semaphore: Semaphore = asyncio.Semaphore(2)  # Allow 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))


asyncio.run(main())