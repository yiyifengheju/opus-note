---
title: ⛄ compare
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 `compare` 方法的使用方法，该方法用于比较两个训练好的 CatBoost 模型。[1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)

### 方法调用格式

```python
compare(model,
        data=None,
        metrics=None,
        ntree_start=0,
        ntree_end=0,
        eval_period=1,
        thread_count=-1,
        tmp_dir=None,
        log_cout=sys.stdout,
        log_cerr=sys.stderr)
```

### 参数说明

#### model

* **描述：** 要比较的 CatBoost 模型。
* **可能类型：** `CatBoost Model`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)

#### metrics

* **描述：** 要计算的指标列表。
* **可能类型：** `list` of `string`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)

#### data

* **描述：** 包含要比较的指标值的数据集。
  * **可能类型：** `catboost.Pool`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)

#### ntree_start

* **描述：** 要减少模型应用或指标计算时使用的树的数量，请将树索引范围设置为 `[ntree_start; ntree_end)`，并将要使用的树的步长设置为 `eval_period`。此参数定义应用模型或计算指标时要使用的第一棵树的索引（范围的包含左边界）。索引从零开始。
  * **可能类型：** `int`
* **默认值：** `0` [1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)

#### ntree_end

* **描述：** 要减少模型应用或指标计算时使用的树的数量，请将树索引范围设置为 `[ntree_start; ntree_end)`，并将要使用的树的步长设置为 `eval_period`。此参数定义应用模型或计算指标时**不**使用的第一棵树的索引（范围的独占右边界）。索引从零开始。
  * **可能类型：** `int`
* **默认值：** `0`（要使用的最后一棵树的索引等于模型中的树的数量减一） [1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)

#### eval_period

* **描述：** 要减少模型应用或指标计算时使用的树的数量，请将树索引范围设置为 `[ntree_start; ntree_end)`，并将要使用的树的步长设置为 `eval_period`。此参数定义应用模型或计算指标时要使用的树的步长。例如，假设设置了以下参数值：
  * `ntree_start` 设置为 `0`
  * `ntree_end` 设置为 `N`（总树数量）
  * `eval_period` 设置为 `2`
    在这种情况下，将为以下树范围计算指标：`[0, 2)`，`[0, 4)`，...，`[0, N)`
  * **可能类型：** `int`
* **默认值：** `1`（树按顺序应用：第一棵树，然后前两棵树，依此类推） [1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)

#### thread_count

* **描述：** 用于操作的线程数。优化执行速度。此参数不影响结果。
  * **可能类型：** `int`
* **默认值：** `-1`（线程数等于处理器核心数） [1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)

#### tmp_dir

* **描述：** 中间结果的临时目录的名称。
  * **可能类型：** `string`
* **默认值：** `None`（名称将被生成） [1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)

#### log_cout

* **描述：** 用于输出标准 C++ 流的对象。
  * **可能类型：** `object`
* **默认值：** `sys.stdout` [1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)

#### log_cerr

* **描述：** 用于输出错误 C++ 流的对象。
  * **可能类型：** `object`
* **默认值：** `sys.stderr` [1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)

### 返回值类型

`compare` 方法返回一个 `pandas.DataFrame`，其中包含两个模型在不同树数量下的指标值。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)

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

model1 = CatBoostClassifier(iterations=100, learning_rate=0.1)
model1.fit(train_dataset, verbose=False)

model2 = CatBoostClassifier(iterations=100, learning_rate=0.3)
model2.fit(train_dataset, verbose=False)

model1.compare(model2, eval_dataset, ['Logloss'])
```

这个示例展示了如何使用 `compare` 方法比较两个 CatBoost 模型在验证数据集上的 `Logloss` 指标。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier_modelcompare)