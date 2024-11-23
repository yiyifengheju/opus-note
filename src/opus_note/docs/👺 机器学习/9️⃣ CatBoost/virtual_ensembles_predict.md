---
title: virtual_ensembles_predict
comments: true
---

`virtual_ensembles_predict` 方法，允许使用虚拟集成方法对给定数据集进行预测。

__方法调用格式：__

```python
virtual_ensembles_predict(model, data, prediction_type=None, virtual_ensembles_count=1, ntree_start=0, ntree_end=0, eval_period=1, thread_count=-1, verbose=None)
```

__参数：__

*   __`model`__:  训练好的 CatBoost 模型。必填参数。
*   __`data`__:  特征值数据。格式取决于输入对象的个数：
    *   多个对象：矩阵状数据，形状为 (object_count, feature_count)。
    *   单个对象：数组。
        数据类型可以是 `catboost.Pool`、列表的列表、`numpy.ndarray`、`pandas.DataFrame`、`pandas.SparseDataFrame`、`pandas.Series`、`catboost.FeaturesData` 或 `scipy.sparse.spmatrix`（除 `dia_matrix` 外的所有子类）。必填参数。[类似于`staged_predict`的参数描述]
*   __`prediction_type`__:  所需的预测类型。支持的预测类型：`Probability`、`Class`、`RawFormulaVal`、`Exponent`、`LogProbability`。默认为 `None` （对于 Poisson 和 Tweedie 损失函数为 `Exponent`，对于所有其他损失函数为 `RawFormulaVal`）。[类似于`staged_predict`的参数描述]
*   __`virtual_ensembles_count`__: 虚拟集成的数量。类型为 `int`，默认为 1。
*   __`ntree_start`__:  要使用的第一棵树的索引（包含在范围内）。索引从 0 开始。默认为 0。[类似于`staged_predict`的参数描述]
*   __`ntree_end`__:  要使用的最后一棵树的索引（不包含在范围内）。默认为 0（表示使用到模型的最后一棵树）。[类似于`staged_predict`的参数描述]
*   __`eval_period`__:  树的步长。类似于 `staged_predict` 中的描述。默认为 1。[类似于`staged_predict`的参数描述]
*   __`thread_count`__:  用于计算预测的线程数。优化执行速度。此参数不影响结果。默认为 -1（线程数等于处理器核心数）。[类似于`staged_predict`的参数描述]
*   __`verbose`__:  是否将测量的评估指标输出到 stderr。默认为 `None`。[类似于`staged_predict`的参数描述]


__返回值：__

一个生成器，它生成使用模型中树的子集依次递增，以及不同虚拟集成组合的预测。生成值的类型取决于输入对象的个数以及 `prediction_type` 参数，类似于 `staged_predict` 的返回值。不同之处在于，`virtual_ensembles_predict` 会为每个虚拟集成生成一组预测。


__虚拟集成方法:__

虚拟集成是一种通过组合多个模型的预测来提高预测准确性的方法。`virtual_ensembles_predict` 方法通过创建多个虚拟集成并对每个集成进行预测来实现这一点。