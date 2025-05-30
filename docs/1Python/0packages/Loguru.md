---
title: 🤣 Loguru
comments: true
---

<img src="https://raw.githubusercontent.com/Delgan/loguru/master/docs/_static/img/demo.gif">

Loguru 是一个 Python 的日志库，它提供了简单易用的 API 和强大的功能，使得在 Python 应用程序中添加日志变得非常容易。

安装：`pip install loguru`

开源地址：https://github.com/Delgan/loguru

## 壹丨基本用法

```python
from loguru import logger

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

> 默认情况下，日志级别为 `INFO`，因此 `logger.debug` 中的消息不会被打印出来。

Loguru 还提供了一些方便的功能，比如将日志消息输出到文件中，以及格式化日志消息。下面是一个带有格式化和文件输出的例子：

```python
from loguru import logger

logger.add("file.log", format="{time} {level} {message}", level="INFO")

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

## 贰丨实例

### 1. 跟踪函数执行时间

Loguru 提供了一个方便的装饰器 `logger.catch`，可以用于捕获函数中的异常，并输出异常信息。可以利用这个特性来跟踪函数的执行时间。

```python
from loguru import logger
import time

@logger.catch
def my_function():
    start_time = time.time()
    # Do something
    end_time = time.time()
    logger.info(f"Execution time: {end_time - start_time} seconds")

my_function()
```

使用 `logger.catch` 装饰器来捕获 `my_function` 函数中的异常，并在函数执行完成后输出函数的执行时间。

### 2. 输出调试信息

有时候，我们需要在代码中输出一些调试信息，比如变量的值或函数的返回值。Loguru 提供了一个方便的 `logger.debug` 方法，可以用于输出调试信息。

```python
from loguru import logger

def my_function(x):
    result = x ** 2
    logger.debug(f"Result: {result}")
    return result

my_function(3)
```

在 `my_function` 函数中使用 `logger.debug` 方法输出了函数的返回值。

### 3. 输出堆栈跟踪信息

当程序发生异常时，我们通常需要输出堆栈跟踪信息来帮助调试。Loguru 提供了一个方便的 `logger.exception` 方法，可以用于输出堆栈跟踪信息。

```python
from loguru import logger

def my_function():
    raise Exception("Oops, something went wrong!")

try:
    my_function()
except Exception:
    logger.exception("An exception occurred:")
```

在 `my_function` 函数中故意抛出了一个异常，并使用 `logger.exception` 方法输出了堆栈跟踪信息。这样可以更好地了解程序发生异常的原因，并帮助调试代码。

































