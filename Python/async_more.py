import asyncio
import random


# Example 1: asyncio.create_task()
async def example_create_task():
    async def background_task(name):
        print(f"Starting {name}")
        await asyncio.sleep(random.uniform(0.1, 0.5))
        print(f"Finished {name}")
        return f"Result from {name}"

    # Create tasks
    task1 = asyncio.create_task(background_task("Task 1"))
    task2 = asyncio.create_task(background_task("Task 2"))

    # Do some other work
    print("Doing other work while tasks are running...")
    await asyncio.sleep(0.3)

    # Wait for tasks to complete
    result1 = await task1
    result2 = await task2
    print(f"Results: {result1}, {result2}")


# Example 2: asyncio.wait()
async def example_wait():
    async def task(name):
        await asyncio.sleep(random.uniform(0.1, 0.5))
        return f"Result from {name}"

    # Create a set of tasks
    tasks = {asyncio.create_task(task(f"Task {i}")) for i in range(5)}

    # Wait for tasks to complete with a timeout
    done, pending = await asyncio.wait(tasks, timeout=0.3)

    print(f"Completed tasks: {len(done)}")
    print(f"Pending tasks: {len(pending)}")

    # Cancel any pending tasks
    for task in pending:
        task.cancel()


# Example 3: asyncio.as_completed()
async def example_as_completed():
    async def task(name, delay):
        await asyncio.sleep(delay)
        return f"{name} completed after {delay:.2f}s"

    tasks = [
        asyncio.create_task(task("Task 1", 0.5)),
        asyncio.create_task(task("Task 2", 0.3)),
        asyncio.create_task(task("Task 3", 0.7)),
    ]

    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        print(result)


# Example 4: asyncio.Queue
async def example_queue():
    queue = asyncio.Queue()

    async def producer():
        for i in range(5):
            await queue.put(f"Item {i}")
            await asyncio.sleep(0.1)

    async def consumer():
        while True:
            item = await queue.get()
            print(f"Consumed: {item}")
            queue.task_done()
            await asyncio.sleep(0.2)

    # Create producer and consumer tasks
    producer_task = asyncio.create_task(producer())
    consumer_task = asyncio.create_task(consumer())

    # Wait for producer to finish
    await producer_task

    # Wait for all items to be processed
    await queue.join()

    # Cancel the consumer
    consumer_task.cancel()


# Run all examples
async def main():
    print("Example 1: asyncio.create_task()")
    await example_create_task()
    print("\nExample 2: asyncio.wait()")
    await example_wait()
    print("\nExample 3: asyncio.as_completed()")
    await example_as_completed()
    print("\nExample 4: asyncio.Queue")
    await example_queue()


asyncio.run(main())
