import asyncio
import time
async def function1():
#    time.sleep(2)
   await asyncio.sleep(2)
   print("funct 1")

async def function2():
#    time.sleep(2)
   await asyncio.sleep(2)
   print("funct 2")

async def function3():
#    time.sleep(2)
   await asyncio.sleep(2)
   print("funct 3")

async def main():
    #gather syntax to perform the many task at once
    L=await asyncio.gather(
       function1(),
       function2(),
       function3(),
    )
    print(L)
    # task =asyncio.create_task(function1)
    # await function1()
    # await function2()
    # await function3()   
asyncio.run(main())    