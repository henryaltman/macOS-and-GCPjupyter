"""
    使用异步 io 可以对无必然顺序要求的多任务进行解耦，减少不必要的阻塞，提高并发度
"""

import asyncio
import time

# # 运行一个协程
# async def main():   # 协程通过 async/await 语法进行声明
#     """
#     打印 "hello"，等待 1 秒，然后打印 "world":
#     """
#     print('hello')
#     await asyncio.sleep(3)
#     print('world')
#
# asyncio.run(main())  # 运行一个协程，asyncio 提供的第一种主要机制:
# # asyncio.run(coro, *, debug=False) 此函数运行传入的协程，
# # 负责管理 asyncio 事件循环并 完结异步生成器。


# #等待一个协程。
# async def say_after(delay,what):
#     await asyncio.sleep(delay)   # sleep() 总是会挂起当前任务，以允许其他任务运行。
#     print(what)
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     await say_after(1,'hello')   # 为什么会先执行完这个子程序，再执行下一个呢
#     await say_after(2,'world')   # 上一个子程序阻塞的时候怎么不跳到这里？因为 send 要传参到里面的 yield
#
#     print(f'finished at {time.strftime(("%X"))}')
#
# asyncio.run(main())
#
# 因为主程序由两个分支组成。子程序处理完后，用 yield 将自己挂起，并返回主程序。
# 主程序通过 send（与 next 方法类似） 唤起子程序并传入数据。如此交替进行。
# """
# 等待 1 秒后打印 "hello"，然后 再次 等待 2 秒后打印 "world":(共需3秒)
# started at 22:21:00
# hello
# world
# finished at 22:21:03
# """


# # 并发 运行 两个 协程:
# async def say_after(delay,what):
#     await asyncio.sleep(delay)
#     print(what)
#
# async def main():
#     """
#     asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程。
#     """
#     task1 = asyncio.create_task(
#         say_after(1,'hello')
#     )
#
#     task2 = asyncio.create_task(
#         say_after(2,'world')
#     )
#     # create_task()方法相当于创建了任务计划，但还没有实施
#     # 返回值 task1 和 task2 是 可等待对象（可在 await 语句中使用）
#
#     print(f'started at {time.strftime("%X")}')
#
#     await task1     # 因为遇到 await 阻塞，跳到其他代码--即"await task2"
#     await task2     # 因为也是 await 阻塞，几乎同时与上一个 await 一起开始等待阻塞结束
#
#     # 执行完以上任务，解阻塞，才向下执行
#     print(f'finished at {time.strftime("%X")}')     # 因为两个 await 几乎同时开始阻塞，所以一共阻塞两秒
#
# asyncio.run(main())


# # 可等待对象
# # 如果一个对象可以在 await 语句中使用，那么它就是 可等待 对象。
# # 主要有三类：协程, 任务 和 Future.
# # 1，协程
# async def nested():  # 定义了一个协程函数 返回 协程对象。
#     return 42
#
# async def main():
#     nested()   # 这语句，什么都不会发生
#
#     print(await nested())   # await 了 一个协程对象（可等待对象）后，才有结果
#
# asyncio.run(main())
#
# # 2，任务
# async def nested():  # 定义了一个协程函数 返回 协程对象。
#     return 42
#
# async def main():
#     # 一个协程通过 asyncio.create_task() 函数被打包为一个 任务，
#     # 该协程将自动排入日程准备立即运行:
#     task = asyncio.create_task(nested())
#
#     await task
#
# # 3, Future 对象
# Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。
# 在应用层不常用


# # 并发运行任务
# async def factorial(name, number):
#     """
#     asyncio.gather(*aws, loop=None, return_exceptions=False)
#     并发 运行 aws 序列中的 可等待对象。
#     """
#     f = 1
#     for i in range(2,number + 1):
#         print(f'Task {name}:Compute factorial({i}).....')
#         await asyncio.sleep(1)
#         f *= i
#     print(f'Task {name}: factorial({number}) = {f}')
#
# async def main():
#     await asyncio.gather(
#         factorial("1",2),
#         factorial("2",3),
#         factorial("3",4)
#     )
#
# asyncio.run(main())