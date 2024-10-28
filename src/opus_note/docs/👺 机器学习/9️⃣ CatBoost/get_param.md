---
title: ⛄ get_param
date: 2024.09.05
comments: true
---

如果用户在开始训练之前明确指定了给定参数的值，则返回该参数的值。如果此参数与默认值一起使用，则此函数返回 None。

使用 [get_all_params](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_all_params)方法获取所有训练参数的值（默认、用户定义和动态计算）。

## 方法调用格式

```
get_param(key)
```

## 参数

key —— 键值

**可能的类型**

string

**默认值**

必需参数

## 返回值类型

指定键的值。如果参数不存在，则返回 None。