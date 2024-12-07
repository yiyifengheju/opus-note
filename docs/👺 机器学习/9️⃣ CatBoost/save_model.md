---
title: ⛄ save_model
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 `save_model` 方法的使用方法，该方法用于将训练好的 CatBoost 模型保存到文件。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_save_model)

### 方法调用格式

```python
save_model(fname,
           format="cbm",
           export_parameters=None,
           pool=None)
```

### 参数说明

#### fname

* **描述：** 输出模型的路径。
* **可能类型：** `string`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_save_model)

#### format

* **描述：** 输出模型的格式。
* **可能的值：**
  * `cbm`：CatBoost 二进制格式。
  * `coreml`：Apple CoreML 格式（目前仅支持没有分类特征的数据集）。
  * `json`：JSON 格式。有关格式详细信息，请参阅 CatBoost JSON 模型教程。
  * `python`：独立的 Python 代码（目前不支持多分类模型）。有关应用结果模型的详细信息，请参阅 Python 部分。
  * `cpp`：独立的 C++ 代码（目前不支持多分类模型）。有关应用结果模型的详细信息，请参阅 C++ 部分。
  * `onnx`：ONNX-ML 格式（目前仅支持没有分类特征的数据集）。有关详细信息，请参阅 [https://onnx.ai/](https://onnx.ai/)。有关应用结果模型的详细信息，请参阅 ONNX 部分。
  * `pmml`：PMML 版本 4.3 格式。如果训练数据集中存在分类特征，则必须在训练期间将它们解释为独热编码。这可以通过将 `--one-hot-max-size` / `one_hot_max_size` 参数设置为大于数据集中所有分类特征的唯一分类特征值的最大数量的值来实现。有关应用结果模型的详细信息，请参阅 PMML 部分。
* **可能类型：** `string`
* **默认值：** `cbm` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_save_model)

#### export_parameters

* **描述：** 针对特定格式的额外参数：
  * **Apple CoreML**
    * `prediction_type`：可能的值为 `probability` 和 `raw`。
    * `coreml_description`
    * `coreml_model_version`
    * `coreml_model_author`
    * `coreml_model_license`
  * **ONNX-ML**
    * `onnx_graph_name`
    * `onnx_domain`
    * `onnx_model_version`
    * `onnx_doc_string`
    * 有关详细信息，请参阅 ONNX-ML 参数参考。
  * **PMML**
    * `pmml_copyright`
    * `pmml_description`
    * `pmml_model_version`
    * 有关详细信息，请参阅 PMML 参数参考。
* **可能类型：** `dict`
* **默认值：** `None` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_save_model)

#### pool

* **描述：** 用于训练的先前数据集。如果模型包含分类特征，并且输出格式为 `cpp`、`python` 或 `JSON`，则此参数是必需的。
* **可能类型：** `catboost.Pool`、`list`、`numpy.ndarray`、`pandas.DataFrame`、`pandas.Series`、`catboost.FeaturesData`
* **默认值：** `None`
* **注意：** 模型可以保存到 `JSON` 格式而无需数据集。在这种情况下，它可供查看，但不可用。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_save_model)

### 返回值类型

`save_model` 方法没有返回值。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_save_model)

### 示例

```python
from catboost import CatBoostClassifier, Pool

# 训练数据
train_data = [[1, 3], [0, 4], [1, 7]]
train_labels = [1, 0, 1]

# 创建数据集
train_pool = Pool(train_data, train_labels)

# 训练模型
model = CatBoostClassifier(learning_rate=0.03)
model.fit(train_pool, verbose=False)

# 保存模型
model.save_model("model")
```

这个示例展示了如何使用 `save_model` 方法将训练好的 CatBoost 模型保存到文件。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_save_model)