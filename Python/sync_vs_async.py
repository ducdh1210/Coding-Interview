import asyncio
import time


# Synchronous Version
def fetch_data(name: str, delay: int) -> str:
    print(f"Start fetching data for {name}")
    time.sleep(delay)  # Simulate an I/O-bound operation
    print(f"Finished fetching data for {name}")
    return f"Data for {name}"


def main_sync():
    start_time = time.time()

    results = []
    for item in [("A", 3), ("B", 2), ("C", 1)]:
        results.append(fetch_data(*item))

    for result in results:
        print(result)

    end_time = time.time()
    print(f"Total time (sync): {end_time - start_time:.2f} seconds")


# Run synchronous version
main_sync()

print("\n" + "=" * 50 + "\n")

# Asynchronous Version


async def fetch_data_async(name: str, delay: int) -> str:
    print(f"Start fetching data for {name}")
    await asyncio.sleep(delay)  # Simulate an I/O-bound operation
    print(f"Finished fetching data for {name}")
    return f"Data for {name}"


async def main_async():
    start_time = time.time()

    tasks = [
        fetch_data_async("A", 3),
        fetch_data_async("B", 2),
        fetch_data_async("C", 1),
    ]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

    end_time = time.time()
    print(f"Total time (async): {end_time - start_time:.2f} seconds")


# Run asynchronous version
asyncio.run(main_async())
