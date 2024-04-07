import asyncio


# This is a coroutine
async def main():
    print("Start of main coroutine")


# Calling coroutine will return a coroutine object
# print(main())

# We have to pass coroutine object to the asyncio's run method for async execution
asyncio.run(main())
