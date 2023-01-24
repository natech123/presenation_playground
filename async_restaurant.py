import time
import asyncio



async def prep_order(meal, prep_time):
    print(f"{meal} is getting made...")
    await asyncio.sleep(prep_time)
    print(f"{meal} is done!")



async def place_orders():
    start = time.time()
    await asyncio.gather(prep_order("Pealla (with all the extras)",5),
     prep_order("mushroom risotto",3),
     prep_order("Cinnamon Bun", 1))

    end = time.time()
    print(f"Total food prep time: {end-start} s")


if __name__ == "__main__":
    asyncio.run(place_orders())
