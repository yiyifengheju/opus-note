---
title: ⛄ plot_predictions
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 `plot_predictions` 方法的使用方法，该方法用于绘制指定特征值变化时模型预测值的图表。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_predictions)

### 方法调用格式

```python
plot_predictions(data,
                 features_to_change,
                 plot=True,
                 plot_file=None)
```

### 参数说明

#### data

* **描述：** 用于绘制预测值的输入数据集。例如，可以使用原始数据集的两个文档切片（参见下面的示例）。
* **可能类型：**
  * `numpy.ndarray`
  * `pandas.DataFrame`
  * `pandas.SparseDataFrame`
  * `scipy.sparse.spmatrix`（除 `dia_matrix` 以外的所有子类）
  * `catboost.Pool`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_predictions)

#### features_to_change

* **描述：** 要改变预测值以绘制图表的数值特征列表。例如，可以通过选择根据预测差异（PredictionDiff）对一对对象预测结果影响最大的前 N 个重要特征来选择所需特征（参见下面的示例）。
* **可能类型：**
  * `list` of `int`
  * `string`
  * `list` of `int` & `string` 的组合
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_predictions)

#### plot

* **描述：** 是否绘制 Jupyter Notebook 图表。
* **可能类型：** `bool`
* **默认值：** `True` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_predictions)

#### plot_file

* **描述：** 要保存图表的输出 HTML 文件名。
* **可能类型：** `string`
* **默认值：** `None`（不保存文件） [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_predictions)

### 返回值类型

`plot_predictions` 方法返回一个字典，包含两个字段：

* **第一个字段：** 包含所有数据集中对象的预测值的字典列表。
* **第二个字段：** 包含每个特征索引和对应特征值桶的预测值列表的字典。

### 示例

```python
import numpy as np
from catboost import Pool, CatBoostClassifier

# 训练数据
train_data = np.random.randint(0, 100, size=(100, 10))
train_label = np.random.randint(0, 1000, size=(100))
train_pool = Pool(train_data, train_label)

# 数据集切片
train_pool_slice = train_pool.slice([2, 3])

# 训练模型
model = CatBoostClassifier()
model.fit(train_pool)

# 获取特征重要性
prediction_diff = model.get_feature_importance(train_pool_slice, type='PredictionDiff', prettified=True)

# 绘制预测值图表
model.plot_predictions(data=train_pool_slice,
                       features_to_change=prediction_diff["Feature Id"][:2],
                       plot=True,
                       plot_file="plot_predictions_file.html")
```

这个示例展示了如何使用 `plot_predictions` 方法绘制指定特征值变化时模型预测值的图表。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_predictions)

**注意：** 仅支持在不包含分类特征的数据集上训练的模型。不支持多分类模式。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_predictions)