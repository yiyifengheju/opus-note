---
title: 平均损失
date: 2024.12.16
comments: true
---

区分一下“累加平均损失”和“累积平均损失”两个概念

| 特征         | 累加平均损失                 | 累积平均损失                     |
| ------------ | ---------------------------- | -------------------------------- |
| **计算时机** | 所有批次处理完毕后           | 每一批次结束后                   |
| **更新方式** | 最终一次计算平均值           | 每次更新平均值                   |
| **结果**     | 整个训练周期的精确平均损失   | 实时更新的近似平均损失           |
| **适用场景** | 需要在训练结束后评估整体性能 | 需要实时监控训练过程中的损失变化 |

### 1. 累加平均损失

__定义__：在整个训练过程中，先累加所有批次的损失，在所有批次都处理完毕后再计算最终的平均损失。

__公式__：


$$
L = \frac{\Sigma_{i=1}^N loss_i}{N}
$$


N是总批次数，loss_i是第i批次的损失。

__实现示例__：

```python
total_loss = 0.0
num_batches = 100

for i in range(num_batches):
    # 假设 loss 是每个批次的损失值
    loss = some_function_to_get_loss(i)
    total_loss += loss.item()

average_train_loss = total_loss / num_batches
print(f"Average Training Loss: {average_train_loss}")
```

__特点__：

- __一次性计算__：只有在所有批次处理完毕后才能得到最终的平均损失。
- __精确__：能够提供整个训练周期内的精确平均损失。
- __适用场景__：适合需要在训练结束后评估整体性能的情况。

### 累积平均损失

__定义__：累积平均损失是指在每一批次结束时，立即更新平均损失，使得平均损失随着批次的增加而不断逼近真实的平均值。这种方法在每个批次后都会更新平均损失。

__公式__：


$$
累积平均损失_i = 累积平均损失_{i-1} + \frac{loss_i-累积平均损失_{i-1}}{i}
$$



 其中 i 是当前批次的索引，loss_i是第 i 批次的损失。

__实现示例__：

```python
train_loss = 0.0
num_batches = 100

for i in range(num_batches):
    # 假设 loss 是每个批次的损失值
    loss = some_function_to_get_loss(i)
    train_loss += (loss.item() - train_loss) / (i + 1)

print(f"Cumulative Average Training Loss: {train_loss}")
```

__特点__：

- __实时更新__：每个批次后都会更新平均损失，提供了实时的平均损失信息。
- __平滑__：由于每次更新都是基于当前损失和之前的累积平均损失，损失曲线更加平滑。
- __适用场景__：适合需要实时监控训练过程中的损失变化的情况。

