---
title: 🦢 predict方法详解
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 predict 方法的使用方法，该方法用于获取训练模型的预测结果。[7](https://catboost.ai/en/docs/concepts/python-reference_catboost_predict)

## 壹丨方法调用格式

```python
predict(data,
        prediction_type='RawFormula',
        ntree_start=0,
        ntree_end=0,
        thread_count=-1,
        verbose=None)
```

## 贰丨参数说明

#### data

* **描述：**  获取预测结果的数据集。
  * **支持的格式：**
    * `catboost.Pool`
    * `list`，`numpy.ndarray`，`pandas.DataFrame`，`pandas.Series`：二维特征矩阵。
    * `pandas.SparseDataFrame`，`scipy.sparse.spmatrix`（`dia_matrix` 除外的所有子类）：二维稀疏特征矩阵。
* **默认值：** 必填参数
* **支持的处理单元：** CPU 和 GPU [7](https://catboost.ai/en/docs/concepts/python-reference_catboost_predict)

#### prediction_type

* **描述：**  返回预测结果的类型。
  * **可能的值：**
    * `RawFormula`：模型预测值（应用损失函数之前）。
    * `Class`:  预测类标签（仅适用于分类问题）。
    * `Probability`: 预测对象属于每个类的概率（仅适用于分类问题）。
    * `Exponent`:  `RawFormula` 值的指数。
* **可能类型：** `string`
* **默认值：** `'RawFormula'`
* **支持的处理单元：** CPU 和 GPU [7](https://catboost.ai/en/docs/concepts/python-reference_catboost_predict)

#### ntree_start

* **描述：**  用于预测的树的起始索引。
* **可能类型：** `int`
* **默认值：** `0`
* **支持的处理单元：** CPU 和 GPU [7](https://catboost.ai/en/docs/concepts/python-reference_catboost_predict)

#### ntree_end

* **描述：**  用于预测的树的最后一个索引。`0` 值对应于最后一棵树。
* **可能类型：** `int`
* **默认值：** `0`
* **支持的处理单元：** CPU 和 GPU [7](https://catboost.ai/en/docs/concepts/python-reference_catboost_predict)

#### thread_count

* **描述：**  用于计算预测结果的线程数。
  * **可能的值：**
    * 整数：使用的线程数。
    * `-1`：使用所有可用的核心。
* **可能类型：** `int`
* **默认值：** `-1`
* **支持的处理单元：** CPU 和 GPU [7](https://catboost.ai/en/docs/concepts/python-reference_catboost_predict)

#### verbose

* **描述：**  是否输出计算预测结果的过程。
* **可能类型：** `bool`
* **默认值：** `None`（使用 CatBoost 类的构造函数中指定的 `verbose` 参数的值）
* **支持的处理单元：** CPU 和 GPU [7](https://catboost.ai/en/docs/concepts/python-reference_catboost_predict)