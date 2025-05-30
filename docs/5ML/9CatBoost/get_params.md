---
title: ⛄ get_params
date: 2024.09.05
comments: true
---

返回用户明确指定的训练参数的值。如果所有参数都使用其默认值，则此函数返回一个空字典。

使用 [get_all_params](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_all_params)方法获取所有训练参数的值（默认、用户定义和动态计算）。

## 方法调用格式

```
get_params()
```

## 返回值类型

字典

包含所有模型参数及其对应值的列表的字典。

格式：

```
{param_key: value}
```

## 示例

```
model.get_params()
# {'iterations': 10, 'learning_rate': 0.1}
```