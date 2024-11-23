---
title: FeaturesData
comments: true
---

`FeaturesData` 类提供了一种高效存储和传递特征数据的方式，以便用于 `Pool` 构造函数，从而加快模型训练速度，尤其是在数据集包含数值型和类别型特征混合的情况下。

[官方文档](https://catboost.ai/en/docs/concepts/python-features-data__desc)

__`FeaturesData` 类的用途:__

`FeaturesData` 类旨在优化特征数据的存储和访问，以便更快地创建 `Pool` 对象。当数据集包含大量数值型和类别型特征时，使用 `FeaturesData` 比直接使用 NumPy 数组、Pandas DataFrame 或 Series 效率更高。对于仅包含数值型特征的数据集，使用 NumPy 数组（`dtype=np.float32`）也能获得相似的性能。

__警告:__

`FeaturesData` 类不对输入数据进行任何检查。只有在确信数据完全正确的情况下才应使用它，以避免额外的检查时间。否则，建议直接将输入数据集和目标变量传递给 `Pool` 类。


__参数:__

* __`num_feature_data`__:  数值型特征数据，以 NumPy 数组的形式提供，形状为 `(object_count, num_feature_count)`，数据类型为 `np.float32`。如果数据集不包含数值型特征，则为 `None`。
* __`cat_feature_data`__:  类别型特征数据，以 NumPy 数组的形式提供，形状为 `(object_count, cat_feature_count)`，数据类型为 `object`。数组元素必须是 `bytes` 类型，并包含 UTF-8 编码的字符串。类别型特征必须以字符串形式传递。使用其他数据类型（例如 `int32`）会引发错误。如果数据集不包含类别型特征，则为 `None`。
* __`num_feature_names`__:  数值型特征的名称，以字符串或 `bytes` 类型的序列提供。如果字符串为 `bytes` 类型，则必须是 UTF-8 编码。如果为 `None`，则 `num_feature_names` 属性将设置为一个空字符串列表。
* __`cat_feature_names`__:  类别型特征的名称，以字符串或 `bytes` 类型的序列提供。如果字符串为 `bytes` 类型，则必须是 UTF-8 编码。如果为 `None`，则 `cat_feature_names` 属性将设置为一个空字符串列表。


__细节:__

在创建的 `Pool` 对象中，特征的顺序为：[数值型特征 (如果存在)][类别型特征 (如果存在)]。应用训练好的模型时，必须按照相同的顺序传递特征数据。


__方法:__

`FeaturesData` 类提供了一些方法来获取数据集的信息，例如特征数量、特征名称和对象数量。这些方法包括：`get_cat_feature_count`、`get_feature_count`、`get_feature_names`、`get_num_feature_count` 和 `get_object_count`。


__使用示例:__

```python
import numpy as np
from catboost import CatBoostClassifier, FeaturesData
# Initialize data
cat_features = [0,1,2]
train_data = FeaturesData(
    num_feature_data=np.array([[1, 4, 5, 6], [4, 5, 6, 7], [30, 40, 50, 60]], dtype=np.float32),
    cat_feature_data=np.array([["a", "b"], ["a", "b"], ["c", "d"]], dtype=object)
)
train_labels = [1,1,-1]
test_data = FeaturesData(
    num_feature_data=np.array([[2, 4, 6, 8], [1, 4, 50, 60]], dtype=np.float32),
    cat_feature_data=np.array([["a", "b"], ["a", "d"]], dtype=object)
)
# Initialize CatBoostClassifier
model = CatBoostClassifier(iterations=2, learning_rate=1, depth=2, loss_function='Logloss')
# Fit model
model.fit(train_data, train_labels)
# Get predicted classes
preds_class = model.predict(test_data)
# Get predicted probabilities for each class
preds_proba = model.predict_proba(test_data)
# Get predicted RawFormulaVal
preds_raw = model.predict(test_data, prediction_type='RawFormulaVal')
```

```python
import numpy as np
from catboost import CatBoostClassifier, FeaturesData, Pool
# Initialize data
train_data = Pool(
    data=FeaturesData(
        num_feature_data=np.array([[1, 4, 5, 6],
                                   [4, 5, 6, 7],
                                   [30, 40, 50, 60]],
                                   dtype=np.float32),
        cat_feature_data=np.array([["a", "b"],
                                   ["a", "b"],
                                   ["c", "d"]],
                                   dtype=object)
    ),
    label=[1, 1, -1]
)
test_data = Pool(
    data=FeaturesData(
        num_feature_data=np.array([[2, 4, 6, 8],
                                   [1, 4, 50, 60]],
                                   dtype=np.float32),
        cat_feature_data=np.array([["a", "b"],
                                   ["a", "d"]],
                                   dtype=object)
    )
)
# Initialize CatBoostClassifier
model = CatBoostClassifier(iterations = 2,
                           learning_rate = 1,
                           depth = 2,
                           loss_function = 'Logloss')
# Fit model
model.fit(train_data)
# Get predicted classes
preds_class = model.predict(test_data)
# Get predicted probabilities for each class
preds_proba = model.predict_proba(test_data)
# Get predicted RawFormulaVal
preds_raw = model.predict(test_data, prediction_type='RawFormulaVal')

```