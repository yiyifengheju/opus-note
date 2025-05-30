---
title: ⛄ get_all_params
date: 2024.09.05
comments: true
---

返回所有训练参数的值（包括用户未明确指定的参数值）。

如果未明确指定参数的值，则将其设置为默认值。在某些情况下，这些默认值会根据数据集属性和用户定义参数的值动态变化。例如，在分类模式下，默认学习率会根据迭代次数和数据集大小而变化。此方法返回所有参数的值，包括在训练期间计算的参数值。

使用 [get_params](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_params)方法仅获取训练前明确指定的参数

## 方法调用格式

```
get_all_params()
```

## 返回值类型

字典

## 例子

```
from catboost import CatBoostRegressor

train_data = [[1, 4, 5, 6],
              [4, 5, 6, 7],
              [30, 40, 50, 60]]

eval_data = [[2, 4, 6, 8],
             [1, 4, 50, 60]]

train_labels = [10, 20, 30]

model = CatBoostRegressor()

model.fit(train_data,
          train_labels,
          verbose=False)

print(model.get_all_params())
print(model.get_params())
```