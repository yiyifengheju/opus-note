---
title: 🏐 calc_feature_statistics方法详解
date: 2024.09.05
comments: true
---

这个页面介绍了 CatBoost 中 `calc_feature_statistics` 方法的使用，该方法用于计算和绘制所选特征的统计信息。[1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)[4](https://catboost.ai/en/docs/concepts/feature-analysis-graph)

## 壹丨绘制统计信息解读：

结果图表的 X 轴包含被分成多个桶的特征值。对于数值特征，桶之间的分割表示模型树中的条件（`feature < value`）。对于分类特征，每个桶代表一个类别。[1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)[4](https://catboost.ai/en/docs/concepts/feature-analysis-graph)

结果图表的 Y 轴包含以下图形：

* 桶中的平均目标（标签）值。
* 桶中的平均预测值。
* 桶中的对象数量。
* 特征不同值上的平均预测值。为了计算它，特征值被连续更改以落入每个输入对象的每个桶中。图形上一个桶的值计算为所有对象在其特征值被更改以落入该桶时的平均值。[1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)

该函数的返回值包含来自这些图形的数据。[1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)

计算使用以下信息：

* 训练好的模型
* 数据集
* 标签值

**注意：** 仅支持具有独热编码分类特征的模型。将 `one_hot_max_size` 参数设置为较大的值，以确保对模型中的所有分类特征应用独热编码。不支持多分类模式。[1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)

## 贰丨方法调用格式

```python
calc_feature_statistics(data,
                        target=None,
                        feature=None,
                        prediction_type=None,
                        cat_feature_values=None,
                        plot=True,
                        max_cat_features_on_plot=10,
                        thread_count=-1,
                        plot_file=None)
```

## 叁丨参数说明

#### data

* **描述：**  用于计算统计信息的数据。
  * **可能类型：** `numpy.ndarray`，`pandas.DataFrame`，`pandas.SparseDataFrame`，`scipy.sparse.spmatrix`（`dia_matrix` 除外的所有子类）
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)

#### target

* **描述：**  来自输入数据的对象的标签值。
  * **可能类型：** `numpy.ndarray`，`pandas.Series`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)

#### feature

* **描述：**  要为其计算统计信息的特征索引、名称或它们的任何组合的列表。
  * **使用示例：**
    * 输出有关索引为 0 的单个特征的信息：`feature=0`
    * 输出有关两个特征的信息，其中一个名为 `age`，第二个索引为 10：`feature=["age", 10]`
  * **可能类型：** `int`，`string`，`int`、`string` 或其组合的列表
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)

#### prediction_type

* **描述：**  用于计算平均预测值的预测类型。
  * **可能的值：** `Probability`，`Class`，`RawFormulaVal`，`Exponent`，`LogProbability`
  * **可能类型：** `string`
* **默认值：** `None`（对于 `Logloss` 和 `CrossEntropy` 为 `Probability`，对于所有其他损失函数为 `RawFormulaVal`） [1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)

#### cat_feature_values

* **描述：**  要为其计算统计信息的分类特征值的列表。如果为分类特征计算统计信息，则可以使用。
  * **可能类型：** `list`，`numpy.ndarray`，`pandas.Series`
* **默认值：** `None`（为分类特征的所有值计算统计信息） [1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)

#### plot

* **描述：**  根据计算的统计信息绘制 Jupyter Notebook 图表。
  * **可能类型：** `bool`
* **默认值：** `True` [1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)

#### max_cat_features_on_plot

* **描述：**  要在单个图表上输出的分类特征的不同值的最大数量。如果所选分类特征采用的不同值多于此参数中设置的值，则会绘制多个图表。
  * **可能类型：** `int`
* **默认值：** `10` [1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)

#### thread_count

* **描述：**  用于计算统计信息的线程数。
  * **可能类型：** `int`
* **默认值：** `-1`（线程数等于处理器核心数） [1](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_calc_feature_statistics)

#### plot_file

* **描述：**  用于保存图表