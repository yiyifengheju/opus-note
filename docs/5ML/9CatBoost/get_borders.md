---
title: ⛄ get_borders
date: 2024.09.05
comments: true
---

返回数值特征的边界列表。

## 方法调用格式

```
get_borders()
```

## 例子

```
from catboost import CatBoostClassifier, Pool

X_train = [[1, 2, 30], [4, 5, 60], [7, 8, 90]]
y_train = [0, 1, 0]

feature_names = ['feature_1', 'feature_2', 'feature_3']

train_pool = Pool(X_train, y_train, feature_names=feature_names)

model = CatBoostClassifier(iterations=10, depth=2, learning_rate=1, loss_function='Logloss',verbose=False)
model.fit(train_pool)

borders = model.get_borders()
print("Borders:", borders)

for feature_name, border in zip(feature_names, borders):
    print(f"Borders for {feature_name}: {borders[border]}")
```