---
title: ⛄ get_evals_result
date: 2024.09.05
comments: true
---

返回训练期间计算的指标值。

仅输出计算指标的值。默认情况下，不会为训练数据集计算以下指标，因此不会输出这些指标：

> PFound、YetiRank、NDCG、YetiRankPairwise、AUC、NormalizedGini、FilteredDCG、DCG

使用`hints=skip_train~false`参数启用计算。有关更多详细信息，请参阅[启用、禁用和配置指标计算](https://catboost.ai/en/docs/concepts/loss-functions#enable-disable-configure-metrics)部分。

## 方法调用格式

```
get_evals_result()
```

## 返回值类型

字典

输出格式：

```
{pool_name: {metric_name_1-1: [value_1, value_2, .., value_N]}, .., {metric_name_1-M: [value_1, value_2, .., value_N]}}
```