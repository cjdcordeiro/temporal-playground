import asyncio
from datetime import datetime, timedelta
from temporalio import workflow, activity
from temporalio.client import Client
from temporalio.worker import Worker

@activity.defn
async def say_hello(name: str) -> str:
    return f"Hello, {name}!"

@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            say_hello, name, schedule_to_close_timeout=timedelta(seconds=5)
        )

async def my_worker():
    # Create client connected to server at the given address
    client = await Client.connect("10.2.228.232:7233")

    # Run the worker
    worker = Worker(client, task_queue="my-task-queue", workflows=[SayHello], activities=[say_hello])
    await worker.run()

#if __name__ == "__main__":
#    asyncio.run(main())
