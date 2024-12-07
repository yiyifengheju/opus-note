---
title: ⛄ eval_metrics
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 `eval_metrics` 方法的使用方法，该方法用于计算指定数据集上的指定指标。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_eval-metrics)

### 方法调用格式

```python
eval_metrics(data,
             metrics,
             ntree_start=0,
             ntree_end=0,
             eval_period=1,
             thread_count=-1,
             log_cout=sys.stdout,
             log_cerr=sys.stderr)
```

### 参数说明

#### data

* **描述：** 包含输入数据集的文件或矩阵。
* **可能类型：** `catboost.Pool`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_eval-metrics)

#### metrics

* **描述：** 要计算的指标列表。
* **可能类型：** `list` of `string`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_eval-metrics)

#### ntree_start

* **描述：** 要减少模型应用或指标计算时使用的树的数量，请将树索引范围设置为 `[ntree_start; ntree_end)`，并将要使用的树的步长设置为 `eval_period`。此参数定义应用模型或计算指标时要使用的第一棵树的索引（范围的包含左边界）。索引从零开始。
  * **可能类型：** `int`
* **默认值：** `0` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_eval-metrics)

#### ntree_end

* **描述：** 要减少模型应用或指标计算时使用的树的数量，请将树索引范围设置为 `[ntree_start; ntree_end)`，并将要使用的树的步长设置为 `eval_period`。此参数定义应用模型或计算指标时**不**使用的第一棵树的索引（范围的独占右边界）。索引从零开始。
  * **可能类型：** `int`
* **默认值：** `0`（要使用的最后一棵树的索引等于模型中的树的数量减一） [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_eval-metrics)

#### eval_period

* **描述：** 要减少模型应用或指标计算时使用的树的数量，请将树索引范围设置为 `[ntree_start; ntree_end)`，并将要使用的树的步长设置为 `eval_period`。此参数定义应用模型或计算指标时要使用的树的步长。例如，假设设置了以下参数值：
  * `ntree_start` 设置为 `0`
  * `ntree_end` 设置为 `N`（总树数量）
  * `eval_period` 设置为 `2`
    在这种情况下，将为以下树范围计算指标：`[0, 2)`，`[0, 4)`，...，`[0, N)`
  * **可能类型：** `int`
* **默认值：** `1`（树按顺序应用：第一棵树，然后前两棵树，依此类推） [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_eval-metrics)

#### thread_count

* **描述：** 用于操作的线程数。优化执行速度。此参数不影响结果。
  * **可能类型：** `int`
* **默认值：** `-1`（线程数等于处理器核心数） [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_eval-metrics)

#### log_cout

* **描述：** 用于输出标准 C++ 流的对象。
  * **可能类型：** `object`
* **默认值：** `sys.stdout` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_eval-metrics)

#### log_cerr

* **描述：** 用于输出错误 C++ 流的对象。
  * **可能类型：** `object`
* **默认值：** `sys.stderr` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_eval-metrics)

### 返回值类型

`eval_metrics` 方法返回一个字典，其中包含每个指标的计算结果。每个指标的值是一个数组，其长度等于 `(ntree_end - ntree_start) / eval_period`。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_eval-metrics)

### 示例

```python
from catboost import Pool, CatBoostClassifier

train_data = [[0, 3],
              [4, 1],
              [8, 1],
              [9, 1]]
train_labels = [0, 0, 1, 1]

eval_data = [[1, 3],
             [4, 2],
             [8, 2],
             [8, 3]]

eval_labels = [1, 0, 0, 1]

train_dataset = Pool(train_data, train_labels)

eval_dataset = Pool(eval_data, eval_labels)

model = CatBoostClassifier(iterations=100, learning_rate=0.1)
model.fit(train_dataset, verbose=False)

model.eval_metrics(eval_dataset, ['Logloss', 'AUC'])
```

这个示例展示了如何使用 `eval_metrics` 方法计算验证数据集上的 `Logloss` 和 `AUC` 指标。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_eval-metrics)