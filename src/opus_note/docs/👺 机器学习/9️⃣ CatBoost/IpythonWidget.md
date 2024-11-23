---
title: CatBoostIpythonWidget
comments: true
---

`CatBoostIpythonWidget` 类，用于在 Jupyter Notebook 或 JupyterLab 环境中交互式可视化 CatBoost 模型训练过程的工具。它允许用户实时监控训练进度、查看指标变化以及调整训练参数，而无需重新运行整个训练过程。

[官方文档](https://catboost.ai/en/docs/concepts/python-reference_catboostipythonwidget)  

__主要功能:__

* __交互式可视化:__  `CatBoostIpythonWidget` 提供了一个交互式界面，实时显示训练过程中的关键指标，例如损失函数值、精度等。用户可以通过拖动滑块或点击按钮来调整参数，并立即观察到这些变化对模型训练的影响。

* __参数调整:__  用户可以在训练过程中动态调整模型参数，例如学习率、树的深度等。这使得用户可以根据训练过程中的表现，对模型进行微调，以获得最佳性能。

* __监控训练进度:__  该工具实时显示训练进度，包括已完成的迭代次数、剩余时间等信息，方便用户了解训练过程的进展情况。

* __集成到 Jupyter 环境:__  `CatBoostIpythonWidget` 无缝集成到 Jupyter Notebook 和 JupyterLab 环境中，使用方便快捷。

__调用方法:__

```python
class MetricVisualizer(train_dirs,
                       subdirs=False)
```

__参数：__

`train_dirs`：训练目录，默认`catboost_info`

`subdirs`：子目录，从指定目录和子目录收集并读取数据


__示例:__

1. 从文件系统根目录训练模型：

```python
from catboost import CatBoostClassifier

cat_features = [0,1,2]

train_data = [["a", "b", 1, 4, 5, 6],
["a", "b", 4, 5, 6, 7],
["c", "d", 30, 40, 50, 60]]

train_labels = [1,1,0]

model = CatBoostClassifier(iterations=20,
loss_function = "CrossEntropy",
train_dir = "crossentropy")

model.fit(train_data, train_labels, cat_features)
predictions = model.predict(train_data)

```

2. 使用训练信息绘制图表

```
import catboost

w = catboost.MetricVisualizer('/crossentropy/')
w.start()
```

> 收集并使用全部信息绘制图表：
>
> ```bash
> import catboost
> 
> w = catboost.MetricVisualizer('/', subdirs=True)
> w.start()
> 
> ```