---
title: ⛄ select_features
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 `select_features` 方法的使用方法，该方法用于从数据集选择最佳特征并丢弃有害特征。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

### 方法调用格式

```python
select_features(
    X,
    y=None,
    eval_set=None,
    features_for_select=None,
    num_features_to_select=None,
    algorithm=None,
    steps=None,
    shap_calc_type=None,
    train_final_model=False,
    verbose=None,
    logging_level=None,
    plot=False,
    log_cout=sys.stdout,
    log_cerr=sys.stderr
)
```

### 参数说明

#### X

* 描述： 输入训练数据集。注意，如果在该类的构造函数中指定了非平凡的 `cat_features` 参数值，CatBoost 会检查构造函数参数中指定的分类特征索引与该 `Pool` 类中的索引是否一致。
* 可能类型： `catboost.Pool`
* 默认值： 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### y

* 描述： 训练数据集的目标变量（换句话说，对象的标签值）。必须以一维或二维数组的形式。数组中的数据类型取决于要解决的机器学习任务：
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
* 可能类型： `list`、`numpy.ndarray`、`pandas.DataFrame`、`pandas.Series`
* 默认值： `None`
* 注意： 如果输入训练数据集（在 `X` 参数中指定）的类型为 `catboost.Pool`，则不要使用此参数。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### eval_set

* 描述： 用于以下过程的验证数据集或数据集：
  * 过拟合检测器
  * 最佳迭代选择
  * 监控指标的变化
* 可能类型：
  * `catboost.Pool`
  * `tuple` (X, y)
  * `string` (数据集文件路径)
* 默认值： `None` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### features_for_select

* 描述： 参与选择的特征。支持以下格式：
  * 包含索引、名称、索引范围、名称范围的列表。例如：`[0, 3, 5, 6, '10-15', 'City', 'Player1-Player11']`。
  * 包含索引、名称、索引范围、名称范围的字符串。值用逗号分隔，例如：`0,3,5,6,10-15,City,Player1-Player11`。
* 可能类型： `list`、`string`
* 默认值： 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### num_features_to_select

* 描述： 要从 `features_for_select` 中选择的特征数量。
* 可能类型： `int`
* 默认值： 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### steps

* 描述： 训练模型的次数。使用更多步骤可以获得更准确的选择。
* 可能类型： `int`
* 默认值： `1` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### algorithm

* 描述： 主要算法是递归特征消除，具有可变特征重要性计算方法：
  * `RecursiveByPredictionValuesChange`：最快的算法，也是最不准确的方法（不推荐用于排序损失）。
  * `RecursiveByLossFunctionChange`：根据准确性/速度平衡，最佳选择。
  * `RecursiveByShapValues`：最准确的方法。
* 可能类型： `EFeaturesSelectionAlgorithm`
* 默认值： `RecursiveByShapValues` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### shap_calc_type

* 描述： SHAP 值计算方法，按准确性排序：
  * `Approximate`
  * `Regular`
  * `Exact`
  * 用于 `RecursiveByLossFunctionChange` 和 `RecursiveByShapValues`。
* 可能类型： `EShapCalcType`
* 默认值： `Regular` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### train_final_model

* 描述： 如果指定，则在特征选择后将使用选定特征训练模型。
* 可能类型： `bool`
* 默认值： `True` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### verbose

* 描述： 启用详细输出。
* 可能类型： `bool`
* 默认值： `None` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### logging_level

* 描述： 日志级别。
* 可能类型： `int`
* 默认值： `None` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### plot

* 描述： 是否绘制结果。
* 可能类型： `bool`
* 默认值： `False` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### log_cout

* 描述： 用于输出标准 C++ 流的对象。
* 可能类型： `object`
* 默认值： `sys.stdout` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

#### log_cerr

* 描述： 用于输出错误 C++ 流的对象。
* 可能类型： `object`
* 默认值： `sys.stderr` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

### 返回值类型

`select_features` 方法返回一个字典，包含以下字段：

* `selected_features`：包含选定特征的索引列表。
* `eliminated_features`：包含被消除特征的索引列表。
* `feature_importances`：包含每个特征重要性的字典。
* `model`：如果 `train_final_model` 参数设置为 `True`，则包含使用选定特征训练的模型。

### 示例

```python
from catboost import CatBoostRegressor, Pool, EShapCalcType, EFeaturesSelectionAlgorithm
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

X, y = make_regression(n_samples=1000, n_features=100, n_informative=20, random_state=0)
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.25, random_state=0)
feature_names = ['F{}'.format(i) for i in range(train_X.shape[1])]
train_pool = Pool(train_X, train_y, feature_names=feature_names)
test_pool = Pool(test_X, test_y, feature_names=feature_names)

model = CatBoostRegressor(iterations=1000, random_seed=0)
summary = model.select_features(
    train_pool,
    eval_set=test_pool,
    features_for_select='0-99',
    num_features_to_select=10,
    steps=3,
    algorithm=EFeaturesSelectionAlgorithm.RecursiveByShapValues,
    shap_calc_type=EShapCalcType.Regular,
    train_final_model=True,
    logging_level='Silent',
    plot=True
)
```

这个示例展示了如何使用 `select_features` 方法从数据集选择最佳特征并丢弃有害特征。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_select_features)

### 图的解读

- 初始点：图的左端表示所有特征都被保留时的损失值。
- 曲线变化：随着特征逐步被移除，损失值会发生变化。曲线的形状可以帮助你理解哪些特征对模型性能影响最大。
  - 平缓上升：如果曲线在某些特征被移除后仍然保持平缓上升，说明这些特征对模型性能的影响较小。
  - 陡峭上升：如果曲线在某些特征被移除后陡峭上升，说明这些特征对模型性能的影响较大。