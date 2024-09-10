---
title: ⛄ load_model
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 `load_model` 方法的使用方法，该方法用于从文件加载训练好的 CatBoost 模型。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_load_model)

### 方法调用格式

```python
load_model(fname, format='cbm')
```

### 参数说明

#### fname

* **描述：** 输入模型的路径。
* **可能类型：** `string`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_load_model)

#### format

* **描述：** 输入模型的格式。
* **可能的值：**
  * `cbm`：CatBoost 二进制格式。
  * `AppleCoreML`：Apple CoreML 格式（目前仅支持没有分类特征的数据集）。
  * `json`：JSON 格式。有关格式详细信息，请参阅 CatBoost JSON 模型教程。
  * `onnx`：ONNX-ML 格式（目前仅支持没有分类特征的数据集）。有关详细信息，请参阅 [https://onnx.ai/](https://onnx.ai/)。有关应用结果模型的详细信息，请参阅 ONNX 部分。
  * `CpuSnapshot`：CatBoost 训练快照格式（目前仅支持 CPU 和没有分类特征的数据集）。
* **可能类型：** `string`
* **默认值：** `cbm` [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_load_model)

### 返回值类型

`load_model` 方法返回一个 `catboost.CatBoostModel` 对象，该对象已从指定文件加载。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_load_model)

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

# 加载模型
from_file = CatBoostClassifier()
from_file.load_model("model")
```

这个示例展示了如何使用 `load_model` 方法从文件加载训练好的 CatBoost 模型。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_load_model)