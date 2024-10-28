---
title: ⛄ set_feature_names
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 `set_feature_names` 方法的使用方法，该方法用于设置模型中所有特征的名称。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_set_feature_names)

### 方法调用格式

```python
set_feature_names(feature_names)
```

### 参数说明

#### feature_names

* **描述：** 一个一维数组，包含每个特征的名称。指定名称的顺序和数量必须与数据集中的特征顺序和数量一致。
* **可能类型：** `ndarray`、`list`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_set_feature_names)

### 示例

```python
from catboost import CatBoost

train_data = [[1, 4, 5, 6],
              [4, 5, 6, 7],
              [30, 40, 50, 60]]

eval_data = [[2, 4, 6, 8],
             [1, 4, 50, 60]]

train_labels = [10, 20, 30]

model = CatBoost()

model.fit(train_data,
          train_labels,
          verbose=False)

print("Original feature names:")
print(model.feature_names_)
print("Changed feature names:")
model.set_feature_names(["feature_1", "feature_2", "feature_3", "feature_4"])
print(model.feature_names_)
```

这个示例展示了如何使用 `set_feature_names` 方法设置模型中所有特征的名称。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_set_feature_names)

**输出：**

```
原始特征名称：
['0', '1', '2', '3']
更改后的特征名称：
['feature_1', 'feature_2', 'feature_3', 'feature_4']
```

**注意：** 该方法可以用于 `CatBoost`、`CatBoostClassifier`、`CatBoostRegressor` 和 `Pool` 类。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_set_feature_names)

**此外，`set_feature_names` 方法还可以用于设置 `Pool` 类中所有特征的名称。** [2](https://catboost.ai/en/docs/concepts/python-reference_pool_set_feature_names)

```python
import numpy as np
from catboost import Pool

train_data = [[76, 'blvd', 41, 50, 7],
              [75, 'today', 57, 0, 48],
              [70, 'letters', 33, 17, 7],
              [72, 'now', 43, 29, 12],
              [60, 'back', 2, 0, 1]]

label_values = [1, 0, 0, 1, 4]

input_pool = Pool(data=train_data,
                  label=label_values,
                  cat_features=[1])

input_pool.set_feature_names(['year', 'name', 'BLBRD', 'CAC', 'OAC'])
```

这个示例展示了如何使用 `set_feature_names` 方法设置 `Pool` 类中所有特征的名称。 [2](https://catboost.ai/en/docs/concepts/python-reference_pool_set_feature_names)

**注意：** 在使用 `set_feature_names` 方法设置特征名称后，可以使用 `get_feature_names` 方法获取特征名称。 [3](https://catboost.ai/docs/concepts/python-features-data_get-feature-names)

```python
from catboost import FeaturesData

fd = FeaturesData(
    num_feature_data=np.array([[1, 4, 5, 6], [4, 5, 6, 7], [30, 40, 50, 60]], dtype=np.float32),
    num_feature_names=['num_feat0', 'num_feat1', 'num_feat2', 'num_feat3'],
    cat_feature_data=np.array([["a", "b"], ["a", "b"], ["c", "d"]], dtype=object),
    cat_feature_names=['cat_feat0', 'cat_feat1']
)

print(fd.get_feature_names())
```

这个示例展示了如何使用 `get_feature_names` 方法获取特征名称。 [3](https://catboost.ai/docs/concepts/python-features-data_get-feature-names)

**最后，需要注意的是，CatBoost 模型的特征名称存储在 JSON 格式中，而不能存储在 CPP 格式中。** [4](https://github.com/catboost/catboost/issues/2102) 因此，在使用 Python 加载 CPP 格式的模型时，特征名称将无法被加载。 [4](https://github.com/catboost/catboost/issues/2102)

**此外，如果在 `cat_features` 参数中指定了特征名称而不是索引，则必须为训练数据集提供特征名称。** [6](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier) 否则，CatBoost 将无法识别分类特征。 [6](https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier)