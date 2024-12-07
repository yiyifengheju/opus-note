---
title: ⛄ get_best_score
date: 2024.09.05
comments: true
---

返回在每个验证数据集上计算的每个指标的最佳结果。

### 方法调用格式

```
get_best_score()
```

### 返回值类型

字典

输出格式：

```
{pool_name_1: {metric_1: value,..., metric_N: value}, ..., pool_name_M: {metric_1: value,..., metric_N: value}
```

例如：

```
{'validation': {'Logloss': 0.6085537606941837, 'AUC': 0.0}}
```

### 示例

```
from catboost import CatBoostClassifier, Pool

train_data = [[0, 3],
              [4, 1],
              [8, 1],
              [9, 1]]

train_labels = [0, 0, 1, 1]

eval_data = [[2, 1],
             [3, 1],
             [9, 0],
             [5, 3]]

eval_labels = [0, 1, 1, 0]

eval_dataset = Pool(eval_data,
                    eval_labels)

model = CatBoostClassifier(learning_rate=0.03,
                           custom_metric=['Logloss',
                                          'AUC:hints=skip_train~false'])

model.fit(train_data,
          train_labels,
          eval_set=eval_dataset,
          verbose=False)

print(model.get_best_score())


```