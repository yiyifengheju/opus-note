---
title: 🥭 PythonGUI编程问题汇总
comments: true
---

### 视频处理中延迟问题

OpenCV在摄像机每次获取新帧时，总是先把上一次读取的帧拿出来先用，再把新帧加入缓存，所以要想获取最新的帧，一定要连续读两次才能读到最新帧。

```python
flag, image = self.cap.read()
flag, image = self.cap.read()
```



### QChart扩展库

```bash
pip install PyQtChart
```

使用技巧：https://blog.csdn.net/u011218356/article/details/88957823
