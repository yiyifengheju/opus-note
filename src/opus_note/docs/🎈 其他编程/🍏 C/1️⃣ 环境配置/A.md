---
title: 🧁 CLion配置
comments: true
---

### 1. 全局宏定义[^1]

> 比如需要加入一个名为`LOCAL`的宏开关

第一步，打开`CMakeLists.txt`

第二步，添加：`add_definitions(-DLOCAL)`

（和传统`CMakeLists.txt`区别在于`-D`）







[^1]: CSDN，@Tanzq-blog，[【Clion】如何使用宏定义](https://blog.csdn.net/qq_46276931/article/details/117910350)