---
title: 🍁 Shapash
date: 2023.12.20
comments: true
---

## 壹丨概述

Shapash旨在让每个人都能解释和理解机器学习。它提供了各种可视化效果，带有清晰明确的标签，易于所有人理解。使用 Shapash，可以生成一个Web 应用程序，简化模型功能之间交互的理解，并允许在本地和全局可解释性之间进行无缝导航。Shapash 通过在综合报告中提供有关任何模型和数据的有价值的信息，为数据科学审计做出贡献。

Shapash 适用于回归、二元分类和多类问题。它与多种模型兼容，包括 Catboost、Xgboost、LightGBM、Sklearn Ensemble、线性模型和 SVM等

开源链接：https://github.com/MAIF/shapash

安装：

```bash
pip install shapash
```

```bash
pip install shapash[report]
```

## 贰丨使用

### 1. 创建`SmartExplainer`对象

```python
from shapash import SmartExplainer
xpl = SmartExplainer(
  model=regressor,
  features_dict=house_dict,  # Optional parameter
  preprocessing=encoder, # Optional: compile step can use inverse_transform method
  postprocessing=postprocess, # Optional: see tutorial postprocessing  
)
```

> 在compile方法中有1个强制参数：Model 你可以在这里声明features dict来指定要显示的标签

> 这里的`regressor`是训练后的模型

### 2. 编译数据集

```py
xpl.compile(
    x=xtest,    
    y_pred=y_pred, # Optional: for your own prediction (by default: model.predict)
    y_target=yTest, # Optional: allows to display True Values vs Predicted Values
    additional_data=xadditional, # Optional: additional dataset of features for Webapp
    additional_features_dict=features_dict_additional, # Optional: dict additional data    
)
```

> 编译方法中有1个强制参数：Dataset

> 这里的`x`输入的是测试集

### 3. 显示输出

```py
app = xpl.run_app()
```

### 4. 生成shapash报告

```py
xpl.generate_report(
    output_file='path/to/output/report.html',
    project_info_file='path/to/project_info.yml',
    x_train=xtrain,
    y_train=ytrain,
    y_test=ytest,
    title_story="House prices report",
    title_description="""This document is a data science report of the kaggle house prices tutorial project.
        It was generated using the Shapash library.""",
    metrics=[{'name': 'MSE', 'path': 'sklearn.metrics.mean_squared_error'}]
)
```

>此步骤允许使用数据集的不同分割以及您使用的指标生成项目的独立 html 报告

### 5. 从训练到部署：SmartPredictor 对象

```python
predictor = xpl.to_smartpredictor()
```

> Shapash 提供了一个 SmartPredictor 对象来部署本地解释的摘要以满足操作需求。它是一个专用于部署的对象，比 SmartExplainer 更轻，并具有额外的一致性检查。SmartPredictor 可以与 API 一起使用或以批处理模式使用。它使用适当的措辞提供预测、详细或总结的本地可解释性。

## 叁丨报错

### 1. UnicodeEncodeError: 'gbk' codec can't encode character '\u25c4' in position 3266591: illegal multibyte sequence

发生在`xpl.generate_report()`中调用的`export_and_save_report()`函数

原因：使用`gbk`编码错误，使用`encode`方法指定编码格式

```py
...
- with open(output_file, "w") as file:
+ with open(output_file, "w", encoding='utf-8') as file:
```

### 2. numpy版本问题

原因：使用的Py 3.11环境中numpy版本为1.25.3，shapash限制了numpy版本不超过1.25

解决方法：找到报错位置，将numpy限制修改到更高数值

### 3. 数据输入问题

使用numpy输入数据会报错，最好转成pandas数据，将特征名标记为列名