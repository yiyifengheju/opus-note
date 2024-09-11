---
title: ⛄ get_feature_importance
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 `get_feature_importance` 方法的使用方法，该方法用于计算和返回特征重要性。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_feature_importance)

### 方法调用格式

```python
get_feature_importance(data=None,
                       reference_data=None,
                       type=FstrType.FeatureImportance,
                       prettified=False,
                       thread_count=-1,
                       verbose=False,
                       log_cout=sys.stdout,
                       log_cerr=sys.stderr)
```

### 参数说明

#### data

* **描述：** 用于计算特征重要性的数据集。所需数据集取决于所选的特征重要性计算类型（在 `type` 参数中指定）：
  * `PredictionValuesChange`：如果模型不包含有关叶子权重的信息，则为 `None` 或与训练时使用的相同数据集。所有使用 CatBoost 版本 0.9 或更高版本训练的模型默认包含叶子权重信息。
  * `LossFunctionChange`：任何数据集。对于大型数据集，特征重要性是在子集上计算的。
  * `PredictionDiff`：对象对的列表。
* **可能类型：** `catboost.Pool`
* **默认值：**  对于 `LossFunctionChange` 和 `ShapValues` 类型的特征重要性以及模型不包含有关叶子权重信息的情况下，此参数为必填参数。
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_feature_importance)

#### reference_data

* **描述：** 用于从可解释树的 AI 中获取独立树 SHAP 值的参考数据：从局部解释到全局理解。如果 `type` 为 `ShapValues` 且 `reference_data` 不为 `None`，则计算独立树 SHAP 值。
* **可能类型：** `catboost.Pool`
* **默认值：** `None`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_feature_importance)

#### type

* **描述：** 要计算的特征重要性类型。
  * **可能的值：**
    * `FeatureImportance`：对于非排序指标等于 `PredictionValuesChange`，对于排序指标等于 `LossFunctionChange`（值由系统自动确定）。
    * `ShapValues`：一个向量，包含每个特征对每个输入对象的预测的贡献以及模型对该对象的预测的期望值（在没有关于该对象的任何知识的情况下，平均预测）。
    * `Interaction`：每个特征对的特征交互强度值。
    * `PredictionDiff`：一个向量，包含每个特征对每个对象对的 `RawFormulaVal` 差异的贡献。
* **可能类型：** `catboost.FstrType`
* **默认值：** `FeatureImportance`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_feature_importance)

#### prettified

* **描述：**  是否以排序的 (特征 ID, 特征重要性) 对列表的形式返回特征重要性。如果选择以下 `type` 参数值之一，则应使用此参数：
  * `PredictionValuesChange`
  * `LossFunctionChange`
* **可能类型：** `bool`
* **默认值：** `False`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_feature_importance)

#### thread_count

* **描述：** 用于计算特征重要性的线程数。优化执行速度。此参数不影响结果。
* **可能类型：** `int`
* **默认值：** `-1`（线程数等于处理器核心数）
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_feature_importance)

#### verbose

* **描述：** 此参数的用途取决于给定值的类型：
  * `bool`：将进度输出到标准输出。适用于 `ShapValues` 类型的特征重要性计算。
  * `int`：日志记录周期。
* **可能类型：** `bool` 或 `int`
* **默认值：** `False`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_feature_importance)

#### log_cout

* **描述：** 用于日志记录的输出流或回调。
* **可能类型：** 可调用 Python 对象，提供 `write()` 方法
* **默认值：** `sys.stdout`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_feature_importance)

#### log_cerr

* **描述：** 用于日志记录的错误流或回调。
* **可能类型：** 可调用 Python 对象，提供 `write()` 方法
* **默认值：** `sys.stderr`
* **支持的处理单元：** CPU 和 GPU [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_get_feature_importance)

### 返回值类型

返回值类型取决于所选的特征强度计算方法：

* `PredictionValuesChange`、`LossFunctionChange` 或 `PredictionValuesChange` 且 `prettified` 参数设置为 `False`：长度为 `[n_features]` 的列表，包含每个特征的浮点型特征重要性值。
* `PredictionValuesChange` 或 `LossFunctionChange` 且 `prettified` 参数设置为 `True`：长度为 `[n_features]` 的列表，包含 (特征 ID (字符串), 特征重要性 (浮点型)) 对，按特征重要性值降序排序。
* `ShapValues`：形状为 `(n_objects, n_features + 1)` 的 `np.array`，包含每个 (对象, 特征) 的浮点型 SHAP 值。
* `Interaction`：长度为 `[n_features]` 的列表，包含三个元素的列表，形式为 (第一个特征索引, 第二个特征索引, 交互分数 (浮点型))。

### 示例

```python
from catboost import CatBoost

model = CatBoost()
model.fit(X_train, Y_train, verbose=False)

res = model.calc_feature_statistics(X_train,
                                    Y_train,
                                    feature=['MedInc', 'HouseAge', 'Latitude'],
                                    plot=True)

importance = model.get_feature_importance()
for fea, imp in zip(X_train.columns, importance):
    print(f'{fea}: {imp}')
```



`catboost.CatBoost.get_feature_importance` 方法的 `type` 参数允许你选择不同的特征重要性计算方法。不同的 `type` 值会使用不同的算法来计算特征的重要性，从而提供不同的视角来理解模型的行为。

### `type` 参数的选项

#### 1. `FeatureImportance`

- **描述**：这是默认的特征重要性计算方法，基于损失函数的特征重要性。
- **计算方法**：通过计算每个特征对损失函数的贡献来确定特征的重要性。
- **适用场景**：适用于大多数情况，提供一个整体的特征重要性视角。

#### 2. `PredictionValuesChange`

- **描述**：基于预测值变化的特征重要性。
- **计算方法**：通过测量每个特征对预测值的变化来确定特征的重要性。
- **适用场景**：当你对特征对预测结果的直接影响感兴趣时，这种方法非常有用。

#### 3. `LossFunctionChange`

- **描述**：基于损失函数变化的特征重要性。
- **计算方法**：通过测量每个特征对损失函数的变化来确定特征的重要性。
- **适用场景**：当你对特征对模型性能的影响感兴趣时，这种方法非常有用。

#### 4. `ShapValues`

- **描述**：基于 SHAP 值的特征重要性。
- **计算方法**：使用 SHAP（SHapley Additive exPlanations）算法来计算特征的重要性。
- **适用场景**：提供一个一致且公平的特征重要性视角，特别适用于解释模型的局部和全局行为。

#### 5. `Interaction`

- **描述**：基于特征交互的特征重要性。
- **计算方法**：通过测量特征之间的交互作用来确定特征的重要性。
- **适用场景**：当你对特征之间的交互作用感兴趣时，这种方法非常有用。

### 示例

```python
from catboost import CatBoostClassifier, Pool

# 示例数据
X_train = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y_train = [0, 1, 0]

# 创建数据池
train_pool = Pool(X_train, y_train)

# 初始化分类器
model = CatBoostClassifier(iterations=10, depth=2, learning_rate=1, loss_function='Logloss')

# 训练模型
model.fit(train_pool, verbose=False)

# 获取不同类型的特征重要性
feature_importance_prediction = model.get_feature_importance(type='PredictionValuesChange')
print("Feature Importance (PredictionValuesChange):", feature_importance_prediction)
feature_importance_loss = model.get_feature_importance(train_pool, type='LossFunctionChange')
print("Feature Importance (LossFunctionChange):", feature_importance_loss)
feature_importance_default = model.get_feature_importance(type='FeatureImportance')
print("Feature Importance (Default):", feature_importance_default)
feature_importance_shap = model.get_feature_importance(train_pool, type='ShapValues')
print("Feature Importance (ShapValues):", feature_importance_shap)
feature_importance_shap_inter = model.get_feature_importance(train_pool, type='ShapInteractionValues')
print("Feature Importance (ShapInteractionValues):", feature_importance_shap_inter)
feature_importance_interaction = model.get_feature_importance(type='Interaction')
print("Feature Importance (Interaction):", feature_importance_interaction)
```