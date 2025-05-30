---
title: ⛄ randomized_search
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 `randomized_search` 方法的使用方法，该方法用于在指定参数范围内随机搜索最佳模型参数。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

### 方法调用格式

```python
randomized_search(param_distributions,
                  X,
                  y=None,
                  cv=3,
                  n_iter=10,
                  partition_random_seed=0,
                  calc_cv_statistics=True,
                  search_by_train_test_split=True,
                  refit=True,
                  shuffle=True,
                  stratified=None,
                  train_size=0.8,
                  verbose=True,
                  plot=False,
                  log_cout=sys.stdout,
                  log_cerr=sys.stderr)
```

### 参数说明

#### param_distributions

* **描述：** 包含参数名称（字符串）作为键，以及要尝试的参数设置分布或列表作为值的字典。分布必须提供 `rvs` 方法用于采样（例如，来自 `scipy.stats.distributions` 的那些）。如果给定列表，则将从该列表中均匀采样。
* **可能类型：** `dict`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### X

* **描述：** 输入训练数据集。
  * **可能类型：**
    * `catboost.Pool`：输入训练数据集。注意，如果在该类的构造函数中指定了非平凡的 `cat_features` 参数值，CatBoost 会检查构造函数参数中指定的分类特征索引与该 `Pool` 类中的索引是否一致。
    * `numpy.ndarray`、`pandas.DataFrame`：输入训练数据集，以二维特征矩阵的形式。
    * `pandas.SparseDataFrame`、`scipy.sparse.spmatrix`（除 `dia_matrix` 以外的所有子类）：输入训练数据集，以二维稀疏特征矩阵的形式。
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### y

* **描述：** 训练数据集的目标变量（换句话说，对象的标签值）。必须以一维或二维数组的形式。数组中的数据类型取决于要解决的机器学习任务：
  * 回归和排序：一维数值数组。
  * 多元回归：二维数值数组。第一个索引用于维度，第二个索引用于对象。
  * 二元分类：包含以下内容之一的一维数组：
    * 布尔值、整数或字符串，表示类的标签（只有两个唯一值）。
    * 数值。数值的解释取决于所选的损失函数：
      * `Logloss`：如果严格大于 `target_border` 训练参数的值，则该值被视为正类。否则，它被视为负类。
      * `CrossEntropy`：该值被解释为数据集对象属于正类的概率。可能的值在 [0; 1] 范围内。
  * 多分类：一维整数或字符串数组，表示类的标签。
  * 多标签分类：二维数组。第一个索引用于标签/类，第二个索引用于对象。可能的值取决于所选的损失函数：
    * `MultiLogloss`：仅允许 {0, 1} 或 {False, True} 值，指定对象是否属于对应于第一个索引的类。
    * `MultiCrossEntropy`：范围在 [0; 1] 内的数值，被解释为数据集对象属于对应于第一个索引的类的概率。
* **可能类型：** `list`、`numpy.ndarray`、`pandas.DataFrame`、`pandas.Series`
* **默认值：** `None`
* **注意：** 如果输入训练数据集（在 `X` 参数中指定）的类型为 `catboost.Pool`，则不要使用此参数。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### cv

* **描述：** 交叉验证拆分策略。此参数的解释取决于输入数据类型：
  * `None`：使用默认的三折交叉验证。
  * `int`：交叉验证中的折数。
  * `(Stratified)KFold` 对象：scikit-learn 拆分器类之一，具有 `split` 方法。
  * 可迭代对象，生成训练和测试拆分作为索引数组。
* **可能类型：** `int`、`scikit-learn splitter object`、`cross-validation generator iterable`
* **默认值：** `None` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### n_iter

* **描述：** 要采样的参数设置数量。此参数权衡运行时间与解决方案的质量。
* **可能类型：** `int`
* **默认值：** `10` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### partition_random_seed

* **描述：** 将此作为数据随机排列的种子值。排列在拆分数据进行交叉验证之前执行。每个种子生成唯一的拆分。
* **可能类型：** `int`
* **默认值：** `0` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### calc_cv_statistics

* **描述：** 使用交叉验证和找到的最佳参数来估计质量。模型使用这些参数进行拟合。如果 `search_by_train_test_split` 参数设置为 `True`，则可以启用此选项。
* **可能类型：** `bool`
* **默认值：** `True` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### search_by_train_test_split

* **描述：** 将源数据集拆分为训练和测试部分。模型在训练部分上进行训练，而参数通过测试数据集上的损失函数得分进行比较。建议对大型数据集启用此选项，而对小型数据集禁用此选项。
* **可能类型：** `bool`
* **默认值：** `True` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### refit

* **描述：** 使用找到的最佳参数在整个数据集上重新拟合估计器。
* **可能类型：** `bool`
* **默认值：** `True` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### shuffle

* **描述：** 打乱数据集对象。
* **可能类型：** `bool`
* **默认值：** `True` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### stratified

* **描述：** 是否对数据进行分层采样。
* **可能类型：** `bool`
* **默认值：** `None` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### train_size

* **描述：** 训练集的大小。
* **可能类型：** `float`
* **默认值：** `0.8` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### verbose

* **描述：** 启用详细输出。
* **可能类型：** `bool`
* **默认值：** `True` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### plot

* **描述：** 是否绘制结果。
* **可能类型：** `bool`
* **默认值：** `False` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### log_cout

* **描述：** 用于输出标准 C++ 流的对象。
* **可能类型：** `object`
* **默认值：** `sys.stdout` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

#### log_cerr

* **描述：** 用于输出错误 C++ 流的对象。
* **可能类型：** `object`
* **默认值：** `sys.stderr` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

### 返回值类型

`randomized_search` 方法返回一个 `catboost.CatBoostModel` 对象，该对象已使用找到的最佳参数进行拟合。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)

### 示例

```python
from catboost import CatBoost

train_data = [[1, 4, 5, 6],
              [4, 5, 6, 7],
              [30, 40, 50, 60],
              [20, 30, 70, 60],
              [10, 80, 40, 30],
              [10, 10, 20, 30]]
train_labels = [10, 20, 30, 15, 10, 25]
model = CatBoost()

grid = {'learning_rate': [0.03, 0.1],
        'depth': [4, 6, 10],
        'l2_leaf_reg': [1, 3, 5, 7, 9]}

randomized_search_result = model.randomized_search(grid,
                                                   X=train_data,
                                                   y=train_labels,
                                                   plot=True)
```

这个示例展示了如何使用 `randomized_search` 方法在指定参数范围内随机搜索最佳模型参数。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_randomized_search)