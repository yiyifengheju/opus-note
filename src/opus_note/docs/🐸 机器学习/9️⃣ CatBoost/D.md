---
title: ⛄ calc_leaf_indexes方法详解
date: 2024.09.05
comments: true
---


这个页面介绍了 CatBoost 中 `calc_leaf_indexes` 方法的使用，该方法返回池中对象被模型树映射到的叶子的索引。[1](https://catboost.ai/docs/concepts/python-reference_catboost_calc_leaf_indexes)

## 壹丨方法调用格式

```python
calc_leaf_indexes(data,
                    ntree_start=0,
                    ntree_end=0,
                    thread_count=-1,
                    verbose=False)
```

## 贰丨参数说明

#### data

* **描述：** 包含输入数据集的文件或矩阵。
  * **可能类型：** `catboost.Pool`
* **默认值：** 必填参数 [1](https://catboost.ai/docs/concepts/python-reference_catboost_calc_leaf_indexes)

#### ntree_start

* **描述：** 要减少模型应用或指标计算时使用的树的数量，请将树索引范围设置为 `[ntree_start; ntree_end)`。此参数定义应用模型或计算指标时要使用的第一棵树的索引（范围的包含左边界）。索引从零开始。
  * **可能类型：** `int`
* **默认值：** `0` [1](https://catboost.ai/docs/concepts/python-reference_catboost_calc_leaf_indexes)

#### ntree_end

* **描述：** 要减少模型应用或指标计算时使用的树的数量，请将树索引范围设置为 `[ntree_start; ntree_end)`，并将要使用的树的步长设置为 `eval_period`。此参数定义应用模型或计算指标时**不**使用的第一棵树的索引（范围的独占右边界）。索引从零开始。
  * **可能类型：** `int`
* **默认值：** `0`（要使用的最后一棵树的索引等于模型中的树的数量减一） [1](https://catboost.ai/docs/concepts/python-reference_catboost_calc_leaf_indexes)

#### thread_count

* **描述：** 用于操作的线程数。优化执行速度。此参数不影响结果。
  * **可能类型：** `int`
* **默认值：** `-1`（线程数等于处理器核心数） [1](https://catboost.ai/docs/concepts/python-reference_catboost_calc_leaf_indexes)

#### verbose

* **描述：** 启用调试日志记录级别。
  * **可能类型：** `bool`
* **默认值：** `False` [1](https://catboost.ai/docs/concepts/python-reference_catboost_calc_leaf_indexes)

### 返回值类型

`leaf_indexes`：形状为 `(对象数量, ntree_end - ntree_start)` 的二维 `numpy.ndarray`，类型为 `numpy.uint32`。第 i 行是第 i 个对象的叶子索引数组。 [1](https://catboost.ai/docs/concepts/python-reference_catboost_calc_leaf_indexes)