---
title: ⛄ get_object_importance
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 `get_object_importance` 方法的使用方法，该方法用于计算训练数据集中每个对象对优化指标的影响。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_object_importance)

### 方法调用格式

```python
get_object_importance(pool,
                      train_pool,
                      top_size=-1,
                      type='Average',
                      update_method='SinglePoint',
                      importance_values_sign='All',
                      thread_count=-1,
                      verbose=False,
                      log_cout=sys.stdout,
                      log_cerr=sys.stderr)
```

### 参数说明

#### pool

* **描述：** 用于计算对象重要性的数据集。
* **可能类型：** `catboost.Pool`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_object_importance)

#### train_pool

* **描述：** 用于训练模型的数据集。
* **可能类型：** `catboost.Pool`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_object_importance)

#### top_size

* **描述：** 定义从训练数据集中返回的最重要对象的数目。返回对象的数目将限制在这个数目以内。
* **可能类型：** `int`
* **默认值：** `-1`（不限制返回对象的数目） [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_object_importance)

#### type

* **描述：** 计算对象重要性的方法。
* **可能的值：**
  * `Average`：训练数据集中每个对象在输入数据集中的每个对象上的分数的平均值。
  * `PerObject`：训练数据集中每个对象在输入数据集中的每个对象上的分数。
* **可能类型：** `string`
* **默认值：** `Average` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_object_importance)

#### update_method

* **描述：** 算法精度方法。
* **可能的值：**
  * `SinglePoint`：最快但精度最低的方法。
  * `TopKLeaves`：指定叶子的数量。值越大，计算越精确，但速度越慢。
  * `AllPoints`：最慢但精度最高的方法。
* **可能类型：** `string`
* **默认值：** `SinglePoint` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_object_importance)

#### importance_values_sign

* **描述：** 定义训练数据集中对象对输入数据集中的对象优化指标值的影响类型。仅输出相应的对象。
* **可能的值：**
  * `Positive`：训练数据集中对象对输入数据集中的对象优化指标值的影响为正。
  * `Negative`：训练数据集中对象对输入数据集中的对象优化指标值的影响为负。
  * `All`：训练数据集中对象对输入数据集中的对象优化指标值的影响为正或负。
* **可能类型：** `string`
* **默认值：** `All` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_object_importance)

#### thread_count

* **描述：** 用于操作的线程数。优化执行速度。此参数不影响结果。
* **可能类型：** `int`
* **默认值：** `-1`（线程数等于处理器核心数） [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_object_importance)

#### verbose

* **描述：** 启用调试日志记录级别。
* **可能类型：** `bool`
* **默认值：** `False` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_object_importance)

#### log_cout

* **描述：** 用于输出标准 C++ 流的对象。
* **可能类型：** `object`
* **默认值：** `sys.stdout` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_object_importance)

#### log_cerr

* **描述：** 用于输出错误 C++ 流的对象。
* **可能类型：** `object`
* **默认值：** `sys.stderr` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_object_importance)

### 返回值类型

`get_object_importance` 方法返回两个列表：

* **第一个列表：** 包含索引的列表，每个索引对应于训练数据集中一个对象。
* **第二个列表：** 包含分数的列表，每个分数对应于训练数据集中一个对象对输入数据集中的每个对象的影响。

### 示例

```python
from catboost import Pool, CatBoostClassifier

train_data = [[0, 3], [4, 1], [8, 1], [9, 1]]
train_labels = [0, 0, 1, 1]

input_data = [[1, 3], [4, 2], [8, 2], [8, 3]]
input_labels = [0, 1, 0, 1]

train_pool = Pool(train_data, train_labels)
input_pool = Pool(input_data,input_labels)

model = CatBoostClassifier(iterations=10, learning_rate=0.1)
model.fit(train_pool, verbose=False)

object_importance = model.get_object_importance(input_pool, train_pool)

print(object_importance)
```

这个示例展示了如何使用 `get_object_importance` 方法计算训练数据集中每个对象对输入数据集中的每个对象的影响。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_object_importance)