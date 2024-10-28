---
title: 🤷🏻 NGBoost总览
date: 2024.08.28
comments: true
---

NGBoost是继xgboost、lightGBM、catboost之后boosting家族的新成员，拥有更高的精度、但是由于计算复杂度高导致训练和推理速度更慢。

官方文档：[User Guide](https://stanfordmlgroup.github.io/ngboost/intro.html)

论文[^2]：https://arxiv.org/abs/1910.03225

## 壹丨NGBoost

 NGBoost（Natural Gradient Boosting）是一种概率预测模型，它结合了梯度提升树和自然梯度下降的思想。

### 1. 技术分析[^3]

> 相对神经网络的方法，梯度提升方法在结构化或表格输入数据的预测准确度方面通常表现更佳。

NgBoost的核心思想是逐次最小化负梯度对数似然（NLL）来构建一个加性模型，允许我们以递增的方式构建复杂的概率模型。NGBoost通过概率预测（包括实值输出）实现梯度提升的预测不确定性估计。自然梯度的使用克服了梯度提升通用概率预测困难的技术挑战。

### 2. 应用场景

1. 风险评估：如金融领域的信贷风险或保险行业的索赔概率预测。
2. 医疗诊断：预测疾病的发生概率。
3. 自然语言处理：对文本分类任务中的置信度进行建模。
4. 时间序列分析：预测未来趋势的概率分布。

## 贰丨NGBoost的超参数[^1]

=== "NGBRegressor"

    ````python
    class NGBRegressor(NGBoost, BaseEstimator):
        def __init__(
            self,
            Dist=Normal,
            Score=LogScore,
            Base=default_tree_learner,
            natural_gradient=True,
            n_estimators=500,
            learning_rate=0.01,
            minibatch_frac=1.0,
            col_sample=1.0,
            verbose=True,
            verbose_eval=100,
            tol=1e-4,
            random_state=None,
            validation_fraction=0.1,
            early_stopping_rounds=None,
        ):
    ````

=== "NGBClassifier"

    ````python
    class NGBClassifier(NGBoost, BaseEstimator):
        def __init__(
            self,
            Dist=Bernoulli,
            Score=LogScore,
            Base=default_tree_learner,
            natural_gradient=True,
            n_estimators=500,
            learning_rate=0.01,
            minibatch_frac=1.0,
            col_sample=1.0,
            verbose=True,
            verbose_eval=100,
            tol=1e-4,
            random_state=None,
        ):
    ````



| 参数                    | 说明         | 默认                                          | 取值                                                         |
| ----------------------- | ------------ | --------------------------------------------- | ------------------------------------------------------------ |
| `Dist`                  | 标签y的分布  | 分类：`Bernoulli` 回归：`Normal`              | 分类：`k_categorical`、`Bernoulli` 回归：`Normal`、`LogNormal`、`Exponential` |
| `Score`                 | 损失函数     | `LogScore`                                    | `LogScore`、`CRPScore`                                       |
| `Base`                  | 基学习器     | `default_tree_learner` (max_depth为3的决策树) | 任意sklearn回归模型                                          |
| `natural_gradient`      | 自然梯度     | `True`                                        | `True`：自然梯度 `False`：常规梯度                           |
| `n_estimators`          | 迭代次数     | `500`                                         | `int`                                                        |
| `learning_rate`         | 学习速率     | `0.01`                                        | `float`                                                      |
| `minibatch_frac`        | 小批量大小   | `1.0`                                         | `float 0~1`                                                  |
| `col_sample`            | 列采样       | `1.0`                                         | `float 0~1` 随机选择特征比例                                 |
| `verbose`               | 可视化       | `True`                                        | `bool`                                                       |
| `verbose_eval`          | 日志详细程度 | `100`                                         | `True`：每个训练周期结束输出训练信息 `False`：不输出任何训练信息 `int`：隔多少个训练周期输出一次 |
| `tol`                   | 损失函数阈值 | `1e-4`                                        | `float` 损失函数变化小于tol时训练停止                        |
| `random_state`          | 随机数种子   | `None`                                        | `int`                                                        |
| `validation_fraction`   | 验证样本比例 | `0.1`                                         | `float` 训练中划分一部分数据评估模型性能                     |
| `early_stopping_rounds` | 提前停止轮次 | `None`                                        | `int` 训练中在指定轮次内没有改善，则停止训练                 |

## 叁丨注意点

1. 不支持类别型变量（Categorical Variable）入模，需要自行编码
2. 不支持确实数据入模，需要自行填充
3. 模型复杂度高，训练、推理速度慢，但通用参数效果依然好



## 参考

[^1]: 博客园，@ds风控，[NGBoost参数详解及实战](https://www.cnblogs.com/Data-Science-Risk-Control/p/17705313.html)
[^2]: CSDN，@学吧学吧终成学霸，[集成学习——NGBoost论文研读与原理理解 ](https://blog.csdn.net/weixin_44750583/article/details/103940140)
[^3]: CSDN，@明俪钧，[探索NgBoost：斯坦福大学的高效概率预测库](https://blog.csdn.net/gitblog_00026/article/details/137004266)