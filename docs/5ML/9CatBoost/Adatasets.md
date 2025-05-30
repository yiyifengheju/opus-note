---
title: datasets
date: 2024.09.05
comments: true
---

## 壹丨Catboost中的数据集

| 数据集名称                                                   | 适用       | 数量                             | 代码 |
| ------------------------------------------------------------ | ---------- | -------------------------------- | ---- |
| [UCI Adult Data Set](https://archive.ics.uci.edu/ml/datasets/Adult) | 二分类     | Train：32561<br>Val：16281       |      |
| [Kaggle Amazon Employee Access Challenge](https://www.kaggle.com/c/amazon-employee-access-challenge/data) | 二分类     | Train：32769<br>Val：58921       |      |
| [Epsilon dataset](https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html#epsilon) | 二分类     | Train：400000<br/>Val：100000    |      |
| [HIGGS Data Set](https://archive.ics.uci.edu/ml/datasets/HIGGS) | 二分类     | Train：10500000<br/>Val：5000000 |      |
| [monotonic1 from Yandex](https://catboost.ai/en/docs/concepts/python-reference_datasets_monotonic1) | 分类、回归 |                                  |      |
| [monotonic2 from Yandex](https://catboost.ai/en/docs/concepts/python-reference_datasets_monotonic2) | 回归       |                                  |      |
| [Microsoft Learning to Rank Dataset](https://www.microsoft.com/en-us/research/project/mslr/) | 排序       | Train：723412<br/>Val：241521    |      |
| [Microsoft Learning to Rank Dataset](https://www.microsoft.com/en-us/research/project/mslr/) | 排序       | Train：10000 <br/>Val：10000     |      |
| [Rotten Tomatoes dataset](https://www.kaggle.com/rpnuser8182/rotten-tomatoes) | 文本分类   | Train：32712 <br/>Val：8179      |      |
| [Kaggle Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data) | 二分类     | Train：891 <br/>Val：418         |      |

```pyhton
# UCI Adult Data Set
from catboost.datasets import adult
adult_train, adult_test = adult()

adult_train.head(3)
```

```pyhton
# Kaggle Amazon Employee Access Challenge
from catboost.datasets import amazon
amazon_train, amazon_test = amazon()

amazon_train.head(3)
```

```pyhton
# Epsilon dataset
from catboost.datasets import epsilon
epsilon_train, epsilon_test = epsilon()
```

```pyhton
# HIGGS Data Set
from catboost.datasets import higgs
higgs_train, higgs_test = higgs()

higgs_train.head(3)
```

```pyhton
from catboost.datasets import monotonic1
monotonic1_train, monotonic1_test = monotonic1()

monotonic1_train.head(3)
```

```pyhton
from catboost.datasets import monotonic2
monotonic2_train, monotonic2_test = monotonic2()

monotonic2_train.head(3)
```

```pyhton
from catboost.datasets import msrank
msrank_train, msrank_test = msrank()

msrank_train.head(3)
```

```pyhton
from catboost.datasets import msrank_10k
msrank_10k_train, msrank_10k_test = msrank_10k()

msrank_10k_train.head(3)
```

```pyhton
from catboost.datasets import rotten_tomatoes
rotten_tomatoes_train, rotten_tomatoes_test = rotten_tomatoes()

rotten_tomatoes_train.head(3)
```

```pyhton
from catboost.datasets import titanic
titanic_train, titanic_test = titanic()

titanic_train.head(3)
```