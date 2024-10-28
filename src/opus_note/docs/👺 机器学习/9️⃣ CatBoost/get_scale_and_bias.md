---
title: ⛄ get_scale_and_bias
date: 2024.09.05
comments: true
---

返回模型的规模和偏差。

这些值会影响应用模型的结果，因为模型预测结果的计算方式如下：
$$
\sum leaf\_values · scale + bias
$$

## 方法调用格式

```
get_scale_and_bias()
```

## 返回值类型

元组

```python
from catboost import CatBoost
import numpy as np

train_data = np.random.randint(1, 100, size=(100, 10))
train_labels = np.random.randint(2, size=100)

model = CatBoost()
print(model.get_scale_and_bias())

model.fit(train_data, train_labels, verbose=False)
print(model.get_scale_and_bias())
```