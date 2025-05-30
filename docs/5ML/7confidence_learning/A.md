---
title: 🍁 置信学习
date: 2024.08.20
comments: true
---


## 壹丨置信学习

置信学习（confident learning，CL）由MIT和Google联合提出[^1]，它通过表征和识别数据集中的标签错误来关注标签质量，其原理是修剪噪声数据、使用概率阈值计数以估计噪声以及对示例进行排名以进行置信度训练。

> 更多参考：[:fontawesome-brands-github: Awesome-Learning-with-Label-Noise](https://github.com/subeeshvasu/Awesome-Learning-with-Label-Noise)

置信学习的优点：

* **提供置信区间**：为每个预测提供置信区间或置信集，增加预测结果的可靠性和解释性。
* **模型无关**：可以与任何机器学习模型结合使用，具有高度的灵活性和广泛的适用性。
* **保证覆盖率**：在给定的置信水平下，理论上保证置信区间包含真实值的概率至少为该置信水平。
* **处理不确定性**：有效量化和处理数据中的不确定性和噪声，帮助决策者更好地理解预测结果。
* **易于实现**：方法简单，易于在现有机器学习模型上进行调整和扩展。

> 注：置信学习找到的“错误标注样本”，不一定是真实错误样本，这是一种基于不确定估计的选择方法

## 贰丨CleanLab：Don't let your data do you dirty.

开源地址：[cleanlab](https://github.com/cleanlab/cleanlab)

API文档：[cleanlab open-source documentation](https://docs.cleanlab.ai/stable/index.html)

安装：

```bash
rye add cleanlab
```


[^1]: Northcutt, C.G., Jiang, L., & Chuang, I.L. (2019). [Confident Learning: Estimating Uncertainty in Dataset Labels](https://arxiv.org/abs/1911.00068). *J. Artif. Intell. Res., 70*, 1373-1411.