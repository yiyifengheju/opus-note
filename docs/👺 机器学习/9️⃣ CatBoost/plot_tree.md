---
title: ⛄ plot_tree
date: 2024.09.05
comments: true
---

这篇文章介绍了 CatBoost 中 `plot_tree` 方法的使用方法，该方法用于可视化 CatBoost 模型中的决策树。[1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_tree)

### 方法调用格式

```python
plot_tree(tree_idx, pool=None)
```

### 参数说明

#### tree_idx

* **描述：** 要可视化的树的索引。
* **可能类型：** `int`
* **默认值：** 必填参数 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_tree)

#### pool

* **描述：** 仅适用于包含浮点型特征的模型。允许传递一个数据集，并使用该数据集中的外部索引对标签特征进行标记。如果未输入数据集，则使用内部索引。例如，对于一个以分号分隔的包含两个特征 `f1;label;f2` 的数据集，外部特征索引分别为 0 和 2，而内部索引分别为 0 和 1。
* **可能类型：** `catboost.Pool`
* **默认值：** `None`
* **注意：** 对于包含独热编码分类特征的模型，此参数为必填参数。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_tree)

### 返回值类型

`plot_tree` 方法返回一个 `graphviz.dot.Digraph` 对象，该对象描述了可视化的树。树的内部节点对应于分割，并指定了分割中使用的因子名称和边界。叶子节点包含树预测的原始值（RawFormulaVal，参见模型值）。对于多分类模型，叶子节点包含 ClassCount 值（总和为零）。叶子节点的类别可以通过获取叶子节点中该值数组的 argMax 来获得。对于 MultiRMSE 模型，叶子节点包含每个标签的一个值。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_tree)

### 示例

```python
import numpy as np
from catboost import CatBoostClassifier, Pool

# 训练数据
train_data = np.random.randint(0, 100, size=(100, 10))
train_label = np.random.randint(0, 1000, size=(100))
train_pool = Pool(train_data, train_label)

# 训练模型
model = CatBoostClassifier(max_depth=2, verbose=False, max_ctr_complexity=1, iterations=2)
model.fit(train_pool)

# 可视化树
model.plot_tree(tree_idx=0, pool=train_pool)
```

这个示例展示了如何使用 `plot_tree` 方法可视化 CatBoost 模型中的决策树。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_tree)

**注意：** 为了使用 `plot_tree` 方法，需要安装 `graphviz` 包。 [1](https://catboost.ai/en/docs/concepts/python-reference_catboost_plot_tree)