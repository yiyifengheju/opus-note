---
title: 🎃 ThreadPoolExecutor按顺序获取结果
comments: true
---

【目标】

按照任务添加的顺序获取结果

【解决方法】

使用`concurrent.futures.Future`对象的`add_done_callback()`方法来注册一个回调函数，并在任务完成时处理结果

【示例】

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_result(future):
    res = future.result()
    params.append(res)

with ThreadPoolExecutor(max_workers=max_workers) as t:
    obj_list = []
    for item in sgpf:
        obj = t.submit(item.run, target)
        obj.add_done_callback(process_result)
        obj_list.append(obj)

# 等待所有任务完成
for item in obj_list:
    item.result()
```

在这个示例中：

1. 定义一个名为`process_result`的回调函数，接收`Future`对象作为参数。
2. 在回调函数中，获取了该`Future`对象的结果，并将其添加到`params`列表中。
3. 在循环中，使用`add_done_callback()`方法为每个提交的任务注册了回调函数`process_result`。
4. 当任务完成时，回调函数被触发，并按照任务添加的顺序处理结果。

> 另外，添加了一个额外的循环，用于等待所有任务完成。（通过调用每个`Future`对象的`result()`方法，确保在继续执行后续代码之前，所有任务都已完成）

