import asyncio

async def producer(queue):
    for i in range(10):
        await queue.put(i)
    print("Producer: 10 ta son qo'yildi")

async def consumer(queue):
    while True:
        try:
            son = await queue.get()
            print(f"Consumer: {son} ni yig'dim")
            queue.task_done()
        except asyncio.CancelledError:
            break

async def main():
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task
    await consumer_task

    await queue.join()
    print("Barcha sonlar yig'ilgan")

asyncio.run(main())
```

Kodni ishga tushirganda, quyidagilar ro'y beradi:

- Producer 10 ta sonni qo'yadi.
- Consumerlar sonlarni yig'adi.
- Barcha sonlar yig'ilgandan keyin "Barcha sonlar yig'ilgan" deb chiqadi.
