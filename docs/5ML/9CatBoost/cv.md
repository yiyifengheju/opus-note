---
title: cv
comments: true
---

`cv`函数用于执行交叉验证。交叉验证是一种评估机器学习模型性能的强大技术，它通过将数据集分成多个子集（folds），在部分数据上训练模型，并在剩余数据上评估模型来评估模型的泛化能力，从而避免过拟合。

[官方文档](https://catboost.ai/en/docs/concepts/python-reference_cv)


__函数签名:__

```python
cv(pool=None, params=None, iterations=None, num_boost_round=None, fold_count=3, nfold=None, inverted=False, partition_random_seed=0, seed=None, shuffle=True, logging_level=None, stratified=None, as_pandas=True, metric_period=None, verbose=None, verbose_eval=None, plot=False, early_stopping_rounds=None, folds=None, type='Classical', return_models=False)
```

__参数详解:__

* __`pool` (或 `dtrain`)__:  用于交叉验证的输入数据集，通常是一个`Pool`对象。这是必需参数。
* __`params`__:  一个字典，包含模型训练所需的所有参数。这是必需参数。需要注意的是，参数`save_snapshot`、`--snapshot-file`和`snapshot_interval`在交叉验证模式下不被支持。
* __`iterations` (或 `num_boost_round`，`n_estimators`，`num_trees`)__:  模型训练的最大迭代次数（或树的数量）。默认为1000。
* __`fold_count` (或 `nfold`)__:  将数据集划分为的折数（folds）。默认为3。
* __`inverted`__:  布尔值，指示是否进行反向交叉验证。如果为`True`，则在测试集上训练模型，在训练集上评估模型。默认为`False`。
* __`partition_random_seed` (或 `seed`)__:  整数，用于控制数据集划分时的随机种子，确保结果的可重复性。默认为0。
* __`shuffle`__:  布尔值，指示是否在划分数据集之前打乱数据顺序。默认为`True`。
* __`logging_level`__:  字符串，指定日志记录级别，控制输出信息的详细程度。
* __`stratified`__:  布尔值，指示是否进行分层采样。如果为`None`，则根据损失函数自动决定。
* __`as_pandas`__:  布尔值，指示是否将结果以pandas DataFrame的形式返回。默认为`True`。
* __`metric_period`__:  整数，指定计算和输出评估指标的频率（迭代次数）。
* __`verbose` (或 `verbose_eval`)__:  控制日志输出的频率和方式。
* __`plot`__:  布尔值，指示是否在Jupyter Notebook环境中绘制指标曲线图。默认为`False`。
* __`early_stopping_rounds`__:  整数，指定提前停止训练的轮数，用于防止过拟合。
* __`folds`__:  自定义的折叠索引，允许用户指定自定义的数据划分方式。
* __`type`__:  字符串，指定交叉验证的类型，默认为'Classical'。
* __`return_models`__:  布尔值，指示是否返回训练好的模型。默认为`False`。


__返回值:__

如果`as_pandas`为`True`，则返回一个pandas DataFrame，包含每次迭代的平均指标值和标准差。否则，返回一个字典，包含相同的信息。如果`return_models`为`True`，则还会返回训练好的模型列表。


__交叉验证过程:__

`cv`函数将数据集分成`fold_count`个子集。对于每个子集，它使用其余子集训练模型，然后使用该子集评估模型性能。最后，它计算所有子集的平均性能指标和标准差，以提供模型性能的可靠估计。

__示例：__

```python
from catboost import Pool, cv

cv_data = [["France", 1924, 44],
           ["USA", 1932, 37],
           ["Switzerland", 1928, 25],
           ["Norway", 1952, 30],
           ["Japan", 1972, 35],
           ["Mexico", 1968, 112]]

labels = [1, 1, 0, 0, 0, 1]

cat_features = [0]

cv_dataset = Pool(data=cv_data,
                  label=labels,
                  cat_features=cat_features)

params = {"iterations": 100,
          "depth": 2,
          "loss_function": "Logloss",
          "verbose": False}

scores = cv(cv_dataset,
            params,
            fold_count=2,
            plot="True")
```

```python
from catboost import Pool, cv

cv_data = [["France", 1924, 44],
           ["USA", 1932, 37],
           ["Switzerland", 1928, 25],
           ["Norway", 1952, 30],
           ["Japan", 1972, 35],
           ["Mexico", 1968, 112]]

labels = [1, 1, 0, 0, 0, 1]

cv_dataset = Pool(data=cv_data,
                  label=labels,
                  cat_features=[0])

params = {"iterations": 100,
          "depth": 2,
          "loss_function": "Logloss",
          "verbose": False,
          "roc_file": "roc-file"}

scores = cv(cv_dataset,
            params,
            fold_count=2)
```