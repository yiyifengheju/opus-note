---
title: ⛄ set_params
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 `set_params` 方法的使用方法，该方法用于设置模型的训练参数。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_set_params)

### 方法调用格式

```python
set_params(**params)
```

### 参数说明

#### params

* **描述：** 一个字典，包含要设置的训练参数。参数名称作为键，参数值作为值。如果省略，则使用默认值。如果设置，则传递的参数列表将覆盖默认值。
* **可能类型：** `dict`
* **默认值：** `None` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_set_params)

### 示例

```python
model.set_params(iterations=500, thread_count=2, use_best_model=True)
```

这个示例展示了如何使用 `set_params` 方法设置模型的训练参数。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_set_params)