---
title: 🐔 fit
comments: true
---

这篇文章介绍了 CatBoost 中 fit 方法的使用方法，该方法用于训练模型。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

**注意：** 要在 GPU 上训练模型，请在类构造函数中将 `task_type` 参数设置为 `GPU`。在 GPU 上训练需要版本为 450.xx 或更高版本的 NVIDIA 驱动程序。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

### 方法调用格式

```python
fit(X,
    y=None,
    cat_features=None,
    text_features=None,
    embedding_features=None,
    pairs=None,
    graph=None,
    sample_weight=None,
    group_id=None,
    group_weight=None,
    subgroup_id=None,
    pairs_weight=None,
    baseline=None,
    use_best_model=None,
    eval_set=None,
    verbose=None,
    logging_level=None,
    plot=False,
    plot_file=None,
    column_description=None,
    verbose_eval=None,
    metric_period=None,
    silent=None,
    early_stopping_rounds=None,
    save_snapshot=None,
    snapshot_file=None,
    snapshot_interval=None,
    init_model=None,
    log_cout=sys.stdout,
    log_cerr=sys.stderr)
```

### 参数说明

一些参数与 CatBoost 类构造函数中指定的参数重复。在这些情况下，为 fit 方法指定的值优先。其余的训练参数必须在 CatBoost 类的构造函数中设置。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### X 

* **描述：**  根据可能的类型组，描述有所不同。
    * `catboost.Pool`：输入训练数据集。
        **注意：** 如果在此类的构造函数中指定了 `cat_features` 参数的非平凡值，则 CatBoost 会检查构造函数参数和此 Pool 类中分类特征索引规范的等效性。
    * `list`，`numpy.ndarray`，`pandas.DataFrame`，`pandas.Series`：二维特征矩阵形式的输入训练数据集。
    * `pandas.SparseDataFrame`，`scipy.sparse.spmatrix`（`dia_matrix` 除外的所有子类）：二维稀疏特征矩阵形式的输入训练数据集。
* **默认值：** 必填参数
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### y

* **描述：** 训练数据集的目标变量（换句话说，对象的标签值）。必须采用一维或二维数组的形式。数组中的数据类型取决于要解决的机器学习任务：
    * 回归和排名：一维数值数组。
    * 多元回归：二维数值数组。第一个索引用于维度，第二个索引用于对象。
    * 二元分类：包含以下内容之一的一维数组：
        * 表示类标签的布尔值、整数或字符串（只有两个唯一值）。
        * 数值。数值的解释取决于所选的损失函数：
            * `Logloss`：如果该值严格大于 `target_border` 训练参数的值，则该值被视为正类。否则，它被视为负类。
            * `CrossEntropy`：该值被解释为数据集对象属于正类的概率。可能的值在 [0; 1] 范围内。
    * 多分类：表示类标签的一维整数或字符串数组。
    * 多标签分类：二维数组。第一个索引用于标签/类，第二个索引用于对象。可能的值取决于所选的损失函数：
        * `MultiLogloss`：仅允许 {0, 1} 或 {False, True} 值，用于指定对象是否属于与第一个索引对应的类。
        * `MultiCrossEntropy`：[0; 1] 范围内的数值，解释为数据集对象属于与第一个索引对应的类的概率。
* **注意：** 如果输入训练数据集（在 `X` 参数中指定）类型为 `catboost.Pool`，请不要使用此参数。
* **可能类型：** `list`，`numpy.ndarray`，`pandas.DataFrame`，`pandas.Series`
* **默认值：** `None`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### cat_features

* **描述：**  分类列索引的一维数组。仅当 `X` 参数是二维特征矩阵（具有以下类型之一：`list`，`numpy.ndarray`，`pandas.DataFrame`，`pandas.Series`）时才使用它。
* **注意：** `cat_features` 参数也可以在类的构造函数中指定。如果是这样，CatBoost 会检查在此方法和类的构造函数中指定的 `cat_features` 参数的等效性。
* **可能类型：** `list`，`numpy.ndarray`
* **默认值：** `None`（所有特征都被视为数值或其他类型，如果精确指定）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### text_features

* **描述：** 文本列索引（指定为整数）或名称（指定为字符串）的一维数组。仅当 `data` 参数是二维特征矩阵（具有以下类型之一：`list`，`numpy.ndarray`，`pandas.DataFrame`，`pandas.Series`）时才使用。如果此数组中的任何元素指定为名称而不是索引，则必须提供所有列的名称。为此，请使用此构造函数的 `feature_names` 参数显式指定它们，或传递在 `data` 参数中指定了列名称的 `pandas.DataFrame`。
* **可能类型：** `list`，`numpy.ndarray`
* **默认值：** `None`（所有特征都被视为数值或其他类型，如果精确指定）
* **支持的处理单元：** CPU 和 GPU [2](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_fit)

#### embedding_features

* **描述：** embedding 列索引（指定为整数）或名称（指定为字符串）的一维数组。仅当 `data` 参数是二维特征矩阵（具有以下类型之一：`list`，`numpy.ndarray`，`pandas.DataFrame`，`pandas.Series`）时才使用。如果此数组中的任何元素指定为名称而不是索引，则必须提供所有列的名称。为此，请使用此构造函数的 `feature_names` 参数显式指定它们，或传递在 `data` 参数中指定了列名称的 `pandas.DataFrame`。
* **可能类型：** `list`，`numpy.ndarray`
* **默认值：** `None`（所有特征都被视为数值或其他类型，如果精确指定）
* **支持的处理单元：** CPU 和 GPU [2](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor_fit)

#### pairs

* **描述：**  用于成对比较的训练数据集。
    * **支持的格式：**
        * `list` / `numpy.ndarray` / `pandas.DataFrame`: 包含对象索引对的三元组（索引、索引、目标）。目标是第一个对象相对于第二个对象的优势。
        * `catboost.PairsData`: 包含对象索引对和目标的类。
* **默认值：** `None`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### graph

* **描述：**  用于图值数据训练的图结构。
    * **支持的格式：**
        * `list` / `numpy.ndarray`: 包含边列表的二维数组。
        * `catboost.GraphData`: 包含图结构的类。
* **默认值：** `None`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### sample_weight

* **描述：**  对象权重。
    * **支持的格式：**
        * `list` / `numpy.ndarray`: 包含对象权重的一维数组。
        * `pandas.Series`: 包含对象权重的 `pandas.Series`。
* **默认值：** `None`（所有对象权重均假定为 1）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### group_id

* **描述：**  对象组。CatBoost 在组内执行有序提升。
    * **支持的格式：**
        * `list` / `numpy.ndarray`: 包含组标识符的一维数组。如果单个对象属于多个组，则其标识符将出现在此数组中多次，每个组对应一次。
        * `pandas.Series`: 包含组标识符的 `pandas.Series`。如果单个对象属于多个组，则其标识符将出现在此数组中多次，每个组对应一次。
* **默认值：** `None`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### group_weight

* **描述：**  组权重。这些权重会影响损失函数中相应组的贡献。
    * **支持的格式：** `list` / `numpy.ndarray`: 包含组权重的一维数组。
* **默认值：** `None`（所有组权重均假定为 1）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### subgroup_id

* **描述：**  对象子组。CatBoost 在子组内执行有序提升。
    * **支持的格式：**
        * `list` / `numpy.ndarray`: 包含子组标识符的一维数组。如果单个对象属于多个子组，则其标识符将出现在此数组中多次，每个子组对应一次。
        * `pandas.Series`: 包含子组标识符的 `pandas.Series`。如果单个对象属于多个子组，则其标识符将出现在此数组中多次，每个子组对应一次。
* **默认值：** `None`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### pairs_weight

* **描述：**  对象对权重。这些权重会影响损失函数中相应对象对的贡献。
    * **支持的格式：** `list` / `numpy.ndarray`: 包含对象对权重的一维数组。
* **默认值：** `None`（所有对象对权重均假定为 1）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### baseline

* **描述：**  初始预测值。
    * **支持的格式：**
        * `list` / `numpy.ndarray`: 包含初始预测值的一维或二维数组。
        * `pandas.DataFrame`: 包含初始预测值的 `pandas.DataFrame`。
* **默认值：** `None`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### use_best_model

* **描述：**  如果在 `eval_set` 参数中传递了验证数据集，则使用此参数指定是否使用验证数据集上获得的最佳模型。
* **可能类型：** `bool`
* **默认值：**
  * 如果在 `eval_set` 参数中传递了验证数据集，则为 `True`。
  * 否则为 `False`。
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### eval_set

* **描述：**  验证数据集。
  * **支持的格式：**
    * `catboost.Pool`: 验证数据集。
    * `list` / `numpy.ndarray` / `pandas.DataFrame` / `pandas.Series`: 二维特征矩阵形式的验证数据集。
    * `tuple`: 包含二维特征矩阵形式的验证数据集及其标签（y）的元组。
    * `list` 的 `list`: 包含多个验证数据集的列表。
* **默认值：** `None`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### verbose

* **描述：**  输出训练过程的频率。
  * **支持的值：**
    * `False`: 不输出训练过程。
    * `True`: 每个迭代后输出训练过程。
    * 整数：每指定迭代次数后输出训练过程。
* **可能类型：** `bool`，`int`
* **默认值：** `True`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### logging_level

* **描述：**  日志详细程度。
  * **可能的值：**
    * `Silent`: 不输出任何日志消息。
    * `Verbose`: 输出所有信息。
    * `Info`: 输出信息消息。
    * `Debug`: 输出调试消息。
* **可能类型：** `string`
* **默认值：** `None`（使用 CatBoost 类的构造函数中指定的 `logging_level` 参数的值）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### plot

* **描述：**  是否可视化训练过程。
* **可能类型：** `bool`
* **默认值：** `False`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### plot_file

* **描述：**  用于保存训练过程可视化结果的文件的名称。
* **可能类型：** `string`
* **默认值：** `None`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### column_description

* **描述：**  包含训练数据集列描述的文件的路径。
* **可能类型：** `string`
* **默认值：** `None`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### verbose_eval

* **描述：**  如果在 `eval_set` 参数中传递了验证数据集，则使用此参数指定输出度量计算结果的频率。
* **可能类型：** `bool`，`int`
* **默认值：** `None`（使用 CatBoost 类的构造函数中指定的 `verbose_eval` 参数的值）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### metric_period

* **描述：**  计算度量的频率。
* **可能类型：** `int`
* **默认值：** `None`（使用 CatBoost 类的构造函数中指定的 `metric_period` 参数的值）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### silent

* **描述：**  是否静默模式。
* **可能类型：** `bool`
* **默认值：** `None`（使用 CatBoost 类的构造函数中指定的 `silent` 参数的值）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### early_stopping_rounds

* **描述：**  如果在 `eval_set` 参数中传递了验证数据集，则使用此参数停止训练，如果在指定的迭代次数内最佳度量值没有改善。
* **可能类型：** `int`
* **默认值：** `None`（使用 CatBoost 类的构造函数中指定的 `early_stopping_rounds` 参数的值）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### save_snapshot

* **描述：**  是否将快照保存到文件中。
* **可能类型：** `bool`
* **默认值：** `None`（使用 CatBoost 类的构造函数中指定的 `save_snapshot` 参数的值）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### snapshot_file

* **描述：**  用于保存快照的文件的名称。
* **可能类型：** `string`
* **默认值：** `None`（使用 CatBoost 类的构造函数中指定的 `snapshot_file` 参数的值）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### snapshot_interval

* **描述：**  保存快照的时间间隔（以秒为单位）。
* **可能类型：** `int`
* **默认值：** `None`（使用 CatBoost 类的构造函数中指定的 `snapshot_interval` 参数的值）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### init_model

* **描述：**  用于初始化模型的模型的路径或模型本身。
* **可能类型：** `string`，`catboost.CatBoost`
* **默认值：** `None`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### log_cout

* **描述：**  用于输出标准 C++ 流的对象。
* **可能类型：** `object`
* **默认值：** `sys.stdout`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)

#### log_cerr

* **描述：**  用于输出错误 C++ 流的对象。
* **可能类型：** `object`
* **默认值：** `sys.stderr`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_fit)