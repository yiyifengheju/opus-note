---
title: 一致性正则化半监督学习
date: 2025.04.12
---


参考：https://lilianweng.github.io/posts/2021-12-05-semi-supervised/



## 壹丨综述

一致性正则化 (Consistency Regularization)，又称一致性训练 (Consistency Training)，假设在给定相同输入的情况下，神经网络内的随机性 (如Dropout)或数据增强变换不会改变模型的预测结果。

## 贰丨模型

Π-model 和 Temporal ensemble都利用一致性约束（Consistency Regularization）来进行半监督学习（Semi-Supervised Learning）[^1]。

![【半监督学习】Π-model、temporal ensemble](https://cdn.ancii.com/article/image/v1/sw/wV/kP/PkwwVsGDmjDG9swnOi7SkjVAsMQAarn73E9S3mmSmcC4fkVgA0cvEqa0s5T9yHi71A9_wfAzBqhJrhWdsD_nXw.png "【半监督学习】Π-model、temporal ensemble")

### 1. Π-model

定义：训练过程每一个 epoch 中，同一个无标签样本前向传播（forward）__两次__，通过数据增强（Data Augmentation）和随机丢弃（Dropout）以注入扰动（或者说随机性、噪声），同一样本的两次前向传播（Forward）会得到不同的预测值（Predictions），Π-model期望这两个Predictions尽可能一致，即模型对扰动鲁棒。

缺点：网络对每个样本运行两次，计算成本高

!!! note "原论文"

【1】Rasmus, A., Berglund, M., Honkala, M., Valpola, H., & Raiko, T. (2015). [Semi-supervised Learning with Ladder Networks](https://arxiv.org/abs/1507.02672). *Neural Information Processing Systems*.

【2】Laine, S., & Aila, T. (2016). [Temporal Ensembling for Semi-Supervised Learning](https://arxiv.org/abs/1610.02242). *ArXiv, abs/1610.02242*.

【3】Sajjadi, M.S., Javanmardi, M., & Tasdizen, T. (2016). [Regularization With Stochastic Transformations and Perturbations for Deep Semi-Supervised Learning](https://arxiv.org/abs/1606.04586). *ArXiv, abs/1606.04586*.

论文【2】正式提出 Π-model，论文【1】提出的是 Γ-model，Π-model 是其简化版。Π-model 在一个 epoch 对每个无标签样本只 forward 两次，而如果是 forward 多次，那么就是论文【3】的方法，所以 Π-model 是 transform/stability 方法的特例。

### 2. Temporal ensemble

定义：训练过程的每一个 epoch 中，同一个无标签样本前向传播（Forward）__一次__，然后使用之前Epochs得到的Predictions来充当另一次Forward。具体做法是用 Moving Average 的方式计算之前Epochs的Predictions，使得Forward次数减少一半，速度提升。

Temporal ensemble的Ensemble是通过Moving Average 来平均之前Epochs的模型输出，隐式地利用了Ensemble。

!!! note "利用Moving Average 能得到当前Epoch下模型准确的Prediction 吗？"

    在训练前期，模型经过一个Epoch 训练提升就很大，这个时候很可能就是不准的，即使Moving Average有集成学习的思想；
    
    在训练后期，模型效果一个Epoch 提升不明显或者较小，这个时候Moving Average得到的Prediction和当前Epoch下的Prediction应该就相近了。
    
    而随训练过程逐渐增大无标签样本权重 （w(t)） 可以解决这个问题。









[^1]: 安科网，@playoffs，[【半监督学习】Π-model、temporal ensemble](https://www.ancii.com/ahb5y4g66/)