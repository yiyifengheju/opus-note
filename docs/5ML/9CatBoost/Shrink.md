---
title: Shrink
comments: true
---

`shrink` 方法用于缩减模型，只保留索引在指定范围内的树。

[官方文档](https://catboost.ai/docs/concepts/python-reference_catboostclassifier_shrink)

__方法调用格式:__

```python
shrink(ntree_end, ntree_start=0)
```

__参数:__

*   `ntree_start`：要保留的第一棵树的索引（从 0 开始）。默认值为 0。类型为整数。
*   `ntree_end`：要保留的最后一棵树的索引（不包含）。换句话说，这是第一棵*不*保留的树的索引。类型为整数，为必填参数。 

__说明:__

`shrink` 方法会缩减模型，只保留索引在 [`ntree_start`, `ntree_end`) 范围内的树。 

__注意:__  缩减后模型的偏差取决于 `ntree_start` 参数的值：

*   如果 `ntree_start` 为 0，则使用原始的偏差值。
*   如果 `ntree_start` 大于 0，则偏差值将设置为 0。