import asyncio
import time
import aiohttp


def log_exec_time(func):
    """Decorator that logs function execution time."""
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        res = await func(*args, **kwargs)
        exec_time = time.time() - start_time
        print(f"Function {func.__name__} was executed at {round(exec_time, 2)} seconds")
        return res
    return wrapper


async def get_reponse(url: str, session: aiohttp.ClientSession):
    """Make asynchronous request to URL."""
    async with session.get(url) as response:
        return response


@log_exec_time
async def make_n_requests(n: int, url: str):
    """Make a specified number of asynchronous requests to a URL."""

    async with aiohttp.ClientSession() as session:
        tasks = []

        for _ in range(n):
            task = asyncio.create_task(get_reponse(url=url, session=session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

        return responses
