---
title: 🐙 Python多线程(二)
comments: true
---

在Python多线程中：

* `join()`方法的作用是线程同步[^1]。
* 守护线程为守护其他线程而设立。被守护的主线程不存在后，守护线程自然消失。

## 壹丨多线程默认情况

默认情况下（`setDaemon(False)`），主线程执行完后立即退出，子线程继续执行直至结束。

```python
import threading
from time import sleep


def threading_1():
    sleep(3)
    print('子线程1结束')


def threading_2():
    sleep(3)
    print('子线程2结束')


if __name__ == '__main__':
    t1 = threading.Thread(target=threading_1)
    t2 = threading.Thread(target=threading_2)
    t1.start()
    t2.start()

    print('主线程结束')
```

运行结果：

```bash
主线程结束
子线程2结束
子线程1结束
```



## 贰丨开启守护线程

为子线程开启守护线程（setDaemon(True)），当主线程结束时，子程序立马结束。

```python
import threading
from time import sleep


def threading_1():
    sleep(3)
    print('子线程1结束')


def threading_2():
    sleep(10)
    print('子线程2结束')


if __name__ == '__main__':
    t1 = threading.Thread(target=threading_1)
    t1.start()

    t2 = threading.Thread(target=threading_2, daemon=True)
    t2.start()

    sleep(5)
    print('主线程结束')
```

> ***Tips：***`t2.setDaemon(True)`方法已弃用，直接在`threading.Thread()`中设置`daemon`属性。

运行结果：

```bash
子线程1结束
主线程结束
```



## 叁丨使用join方法设置同步

子线程使用`join()`方法后，主线程将被阻塞，直至子线程执行结束。将所有子线程放在一个列表依次使用`join()`方法，保证全部子线程能运行完成，主线程才退出。

```python
import threading
from time import sleep


def threading_1():
    sleep(3)
    print('子线程1结束')


def threading_2():
    sleep(10)
    print('子线程2结束')


if __name__ == '__main__':
    threads = []
    t1 = threading.Thread(target=threading_1)
    threads.append(t1)
    t1.start()

    t2 = threading.Thread(target=threading_2, daemon=True)
    threads.append(t2)
    t2.start()

    [thread.join() for thread in threads]

    sleep(1)
    print('主线程结束')
```

运行结果：

```bash
子线程1结束
子线程2结束
主线程结束
```



## 肆丨不设置守护但对`join()`设置超时

给`join()`方法添加`timeout`参数，主线程对每个子线程的等待时间不大于`timeout`值

```python
import threading
from time import sleep


def threading_1():
    sleep(3)
    print('子线程1结束')


def threading_2():
    sleep(10)
    print('子线程2结束')


if __name__ == '__main__':
    threads = []
    t1 = threading.Thread(target=threading_1)
    threads.append(t1)
    t1.start()

    t2 = threading.Thread(target=threading_2, daemon=False)
    threads.append(t2)
    t2.start()

    [thread.join(5) for thread in threads]

    sleep(1)
    print('主线程结束')
```

运行结果：

```bash
子线程1结束
主线程结束
子线程2结束
```

> ***Tips：***主线程在子线程未执行结束就开始执行。由于未设置守护，子线程2会执行至结束。



## 伍丨开启守护并对`join()`设置超时

为子线程2添加守护，并设置`join()`超时。子线程2未在限定时间内执行结束，会被直接终止。

```bash
import threading
from time import sleep


def threading_1():
    sleep(3)
    print('子线程1结束')


def threading_2():
    sleep(10)
    print('子线程2结束')


if __name__ == '__main__':
    threads = []
    t1 = threading.Thread(target=threading_1)
    threads.append(t1)
    t1.start()

    t2 = threading.Thread(target=threading_2, daemon=True)
    threads.append(t2)
    t2.start()

    [thread.join(5) for thread in threads]

    sleep(1)
    print('主线程结束')
```

运行结果：

```bash
子线程1结束
主线程结束
```



[^1]: CSDN，@玖艺东哥，[Python 多线程中的join用法](https://blog.csdn.net/HaidongDU/article/details/112795797)
