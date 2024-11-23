---
title: staged_predict
comments: true
---

`staged_predict` 方法，允许应用训练好的模型，并针对模型的每一棵树计算结果，但只考虑索引在指定范围内的树。

[官方文档](https://catboost.ai/en/docs/concepts/python-reference_catboost_staged_predict)

__方法调用格式：__

```python
staged_predict(data, prediction_type=None, ntree_start=0, ntree_end=0, eval_period=1, thread_count=-1, verbose=None)
```

__参数：__

*   __`data`__:  特征值数据。格式取决于输入对象的个数：
    *   多个对象：矩阵状数据，形状为 (object_count, feature_count)。
    *   单个对象：数组。
        数据类型可以是 `catboost.Pool`、列表的列表、`numpy.ndarray`、`pandas.DataFrame`、`pandas.SparseDataFrame`、`pandas.Series`、`catboost.FeaturesData` 或 `scipy.sparse.spmatrix`（除 `dia_matrix` 外的所有子类）。必填参数。 


*   __`prediction_type`__:  所需的预测类型。支持的预测类型：`Probability`、`Class`、`RawFormulaVal`、`Exponent`、`LogProbability`。默认为 `None` （对于 Poisson 和 Tweedie 损失函数为 `Exponent`，对于所有其他损失函数为 `RawFormulaVal`）。 

*   __`ntree_start`__:  要使用的第一棵树的索引（包含在范围内）。索引从 0 开始。默认为 0。 

*   __`ntree_end`__:  要使用的最后一棵树的索引（不包含在范围内）。默认为 0（表示使用到模型的最后一棵树）。 

*   __`eval_period`__:  树的步长。例如，如果 `ntree_start` 为 0，`ntree_end` 为 N（树的总数），`eval_period` 为 2，则返回的树的范围是 \[0, 2), \[0, 4), ..., \[0, N)。默认为 1（表示依次应用树：第一棵树，然后是前两棵树，以此类推）。 

*   __`thread_count`__:  用于计算预测的线程数。优化执行速度。此参数不影响结果。默认为 -1（线程数等于处理器核心数）。 

*   __`verbose`__:  是否将测量的评估指标输出到 stderr。默认为 `None`。 

__返回值：__

一个生成器，它生成使用模型中树的子集依次递增的预测。生成值的类型取决于输入对象的个数：

*   单个对象：返回值取决于 `prediction_type` 参数的值：
    *   `RawFormulaVal`：原始公式值。
    *   `Class`：类别标签。
    *   `Probability`：一维 `numpy.ndarray`，包含每个类别的概率。

*   多个对象：返回值取决于 `prediction_type` 参数的值：
    *   `RawFormulaVal`：一维 `numpy.ndarray`，包含每个对象的原始公式值。
    *   `Class`：一维 `numpy.ndarray`，包含每个对象的类别标签。
    *   `Probability`：二维 `numpy.ndarray`，形状为 (对象数, 类别数)，包含每个对象每个类别的概率。 

__注意：__ 只有当带有特征值的 `data` 参数包含模型中使用的所有特征时，模型预测结果才会正确。通常，这些特征的顺序必须与训练期间提供的相应列的顺序匹配。但是，如果在训练期间和应用模型时都提供了特征名称，则它们可以通过名称而不是列顺序进行匹配。 [4](https://catboost.ai/docs/concepts/python-reference_catboostclassifier_predict)