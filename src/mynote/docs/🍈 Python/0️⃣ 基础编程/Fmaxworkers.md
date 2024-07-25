---
title: 🦀 `ThreadPoolExecutor`确定可使用的最大`max_workers`
date: 2024.07.24
comments: true
---

`ThreadPoolExecutor`中`max_workers`参数决定了线程池中可以同时运行的最大线程数。选择合适的 `max_workers` 数量可以提高程序的性能和资源利用率。

## 壹丨确定 `max_workers` 的方法

### 1. CPU 密集型任务
对于 CPU 密集型任务（如计算密集型操作），线程数不应超过 CPU 核心数。过多的线程会导致频繁的上下文切换，反而降低性能。

```python
import os
from concurrent.futures import ThreadPoolExecutor

num_cpus = os.cpu_count()
with ThreadPoolExecutor(max_workers=num_cpus) as executor:
    # 提交任务
    pass
```

### 2. I/O 密集型任务
对于 I/O 密集型任务（如文件读写、网络请求），可以使用更多的线程，因为这些任务大部分时间都在等待 I/O 操作完成。一个常见的经验法则是使用`2 * num_cpus`或更多的线程。

```python
import os
from concurrent.futures import ThreadPoolExecutor

num_cpus = os.cpu_count()
max_workers = num_cpus * 2
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    # 提交任务
    pass
```

### 3. 混合型任务
如果任务既包含 CPU 密集型操作又包含 I/O 操作，可以根据任务的具体情况进行调整。可以先从 `num_cpus` 或 `2 * num_cpus` 开始，然后根据实际性能进行调整。

## 贰丨经验总结

```python title="koko_learn.PicTools._base.py"
class THREAD_PARAM:
    NUM_CPUS = os.cpu_count()
    MAX_WORKERS = NUM_CPUS * 2
```

```python title="koko_learn.PicTools._raf.py"
from koko_learn.PicTools._base import THREAD_PARAM

def get_pics(self, path, max_workers=THREAD_PARAM.MAX_WORKERS): # 视情况而定
	...
    t = ThreadPoolExecutor(max_workers=max_workers)
    ...
```