# import asyncio
#
#
# import time
#
#
# now_time = time.perf_counter()
#
# async def main3(name):
#     await asyncio.sleep(8)
#     print(name)
# async  def main2(name):
#     await asyncio.sleep(5)
#     print(name)
#
#
# async  def main(name):
#     await asyncio.sleep(5)
#     print(name)
#
#
#
#
#
# async def runner():
#     task1= asyncio.create_task(main('main1'))
#     task2 = asyncio.create_task(main2("main2"))
#     task3 =  asyncio.create_task(main3('main3'))
#     await asyncio.gather(*[task1,task2,task3])
#
#
# asyncio.run(runner())
# print(time.perf_counter()-now_time)



import threading as thread
import time

def main3(name):
    time.sleep(1)
    print(name)


def main2(name):
    time.sleep(1)
    print(name)



def main(name):
    time.sleep(1)
    print(name)



thread1 = thread.Thread(target = main,args= ('main__1',))
thread2 = thread.Thread(target = main2,args=('main__2',))
thread3 = thread.Thread(target = main3,args= ('main__3',))


thread1.start()
thread2.start()
thread3.start()


thread1.join()
thread2.join()
thread3.join()



for _ in range(8):
    print(_)

