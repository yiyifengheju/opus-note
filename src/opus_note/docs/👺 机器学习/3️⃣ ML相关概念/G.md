---
title: 线性模型
date: 2024.10.20
comments: true
---

!!! warning "以下内容由AI生成"

普通最小二乘法带来的局限性，导致许多时候都不能直接使用其进行线性回归拟合。特别是以下两种情况：

- 数据集的列（特征）数量 > 数据量（行数量），即系数矩阵X不是列满秩。
- 数据集列（特征）数据之间存在较强的线性相关性，即模型容易出现过拟合。

### 1. 岭回归

岭回归向损失函数中添加L2正则项，防止出现过拟合

```
sklearn.linear_model.Ridge(alpha=1.0, fit_intercept=True, normalize=False, copy_X=True, max_iter=None, tol=0.001, solver='auto', random_state=None)
```

- `alpha`: 正则化强度，默认为 1.0。
- `fit_intercept`: 默认为 True，计算截距项。
- `normalize`: 默认为 False，不针对数据进行标准化处理。
- `copy_X`: 默认为 True，即使用数据的副本进行操作，防止影响原数据。
- `max_iter`: 最大迭代次数，默认为 None。
- `tol`: 数据解算精度。
- `solver`: 根据数据类型自动选择求解器。
- `random_state`: 随机数发生器。

> 包含截距项：模型自动计算截距，适用大多数情况
>
> 不包含截距项：适用数据已经中心化的情况

### 2. LASSO回归

LASSO 回归添加是 1 正则项

```
sklearn.linear_model.Lasso(alpha=1.0, fit_intercept=True, normalize=False, precompute=False, copy_X=True, max_iter=1000, tol=0.0001, warm_start=False, positive=False, random_state=None, selection='cyclic')
```

- `alpha`: 正则化强度，默认为 1.0。
- `fit_intercept`: 默认为 True，计算截距项。
- `normalize`: 默认为 False，不针对数据进行标准化处理。
- `precompute`: 是否使用预先计算的 Gram 矩阵来加速计算。
- `copy_X`: 默认为 True，即使用数据的副本进行操作，防止影响原数据。
- `max_iter`: 最大迭代次数，默认为 1000。
- `tol`: 数据解算精度。
- `warm_start`: 重用先前调用的解决方案以适合初始化。
- `positive`: 强制系数为正值。
- `random_state`: 随机数发生器。
- `selection`: 每次迭代都会更新一个随机系数。