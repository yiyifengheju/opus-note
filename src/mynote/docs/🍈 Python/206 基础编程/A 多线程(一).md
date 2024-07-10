---
title: A Python多线程(一)
comments: true
---

> ***Tips：***多线程与多进程是两个概念。

TODO

## 壹丨创建多线程[^2]

### 1. 简单创建

```python
import time
import threading


def run(num_thread):
    print(f"线程{num_thread}")
    time.sleep(2)


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=run, args=(i,))
        t.start()
```

使用`threading.Thread`创建对象，但不会创建线程。当调用`t.start()`时创建并启动子线程。

### 2. 继承`Thread`类（适用于复杂逻辑）

重写`run()`方法，同样使用`t.start()`方法创建并启动子线程。

```python
import threading
from time import sleep


class MyThread(threading.Thread):
    def run(self):
        [sleep(1) for _ in range(3)]


if __name__ == '__main__':
    t = MyThread()
    t.start()
```



## 贰丨查看线程数量

### 1. `enumerate()`方法

通过调用`threading`中的`enumerate()`方法，返回程序中线程列表，包括主线程。

```python
import threading
from time import sleep


def thread_1():
    [sleep(1) for _ in range(3)]


def thread_2():
    [sleep(1) for _ in range(3)]


if __name__ == '__main__':
    t1 = threading.Thread(target=thread_1)
    t2 = threading.Thread(target=thread_2)
    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        print(f'当前运行的线程数为：{length}')
        if length <= 1:
            break
        sleep(0.5)
```

### 2. `active_count()`方法

将上述代码换为：

```python
...
    while True:
        length = threading.active_count()
        print(f'当前运行的线程数为：{length}')
...
```



## 叁丨`join()`方法

当需要子线程运行完主线程继续向下执行时，子线程可以调用`join()`方法，主线程会等待子线程终止或超时再继续执行。

```python
import threading
from time import sleep


def my_thread(name):
    print(f'子线程{name}')
    sleep(2)


if __name__ == '__main__':
    threads = []
    for idx in range(5):
        t = threading.Thread(target=my_thread,args=(idx,))
        threads.append(t)
        t.start()
    [thread.join() for thread in threads]
    print('主线程。。。')
```



## 肆丨控制线程数量[^1]

不限制线程数量，会导致电脑卡死。使用`threading`模块的`Semaphore`类或`BoundedSemaphore`类限制线程数量。初始化`Semaphore()`会给计数器一个值，每调用一次`acquire()`，计数器减1，每调用一次`release()`，计数器加1，当计数器为0时，`acquire()`调用被阻塞。

首先，定义最大线程数量

```python
max_threads = 5
pool_sema = BoundedSemaphore(value=max_threads)
```

然后，在子线程方法中添加线程数限制：

```python
import threading
from time import sleep

max_threads = 20
pool_sema = threading.BoundedSemaphore(value=max_threads)


def my_thread(name):
    with pool_sema:
        print(f'子线程{name}')
        sleep(2)


if __name__ == '__main__':
    for idx in range(100):
        t = threading.Thread(target=my_thread,args=(idx,))
        t.start()

    while True:
        num = threading.active_count()
        print(f'当前运行的线程数为：{num}')
        if num <= 1:
            break
        sleep(0.5)
```

可以使用上述`with`语句，相当于先调用`acquire()`，离开`with`块后自动调用`release()`。

同样地，可以直接使用`acquire()`和`release()`

```python
def my_thread(name):
    pool_sema.acquire()
    print(f'子线程{name}')
    sleep(2)
    pool_sema.release()
```

`BoundedSemaphore`继承自`Semaphore`，功能和 `Semaphore`基本一样。`BoundedSemaphore`使用`release()`时会判断当前信号量的值，如果当前值大于等于初始值，就会抛出错误，而`Semaphore`并不会抛出异常[^3][^4]

## 伍丨Lock和RLock

## 陆丨Event事件

> 未涉及到，暂不整理





[^1]: 博客园，@我是冰霜，[python多线程：控制线程数量](https://www.cnblogs.com/hanmk/p/12990017.html)
[^2]: CSDN，@淋巴不想动，[python-实现多线程的三种方法](https://blog.csdn.net/weixin_43067754/article/details/86763905)
[^3]: CSDN，@viziviuz，[Python 多线程、守护进程、同时运行最大线程数、锁、线程阻塞(线程暂停和继续)](https://blog.csdn.net/qq_42886289/article/details/122177552)
[^4]: 腾讯云，@堕落飞鸟，[十、python学习笔记-线程-线程的start和join](https://cloud.tencent.com/developer/article/1935268)
