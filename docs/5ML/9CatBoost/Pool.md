---
title: Pool
comments: true
---

`Pool` 类是 CatBoost 模型训练和预测的核心数据结构。`Pool` 对象用于存储和管理训练数据、标签以及其他元数据，例如权重、类别特征索引等。使用 `Pool` 对象可以显著提高 CatBoost 模型的训练效率。

[官方文档](https://catboost.ai/en/docs/concepts/python-reference_pool)  

__`Pool` 类的用途:__

`Pool` 类提供了一种高效的方式来组织和传递数据给 CatBoost 模型。它将特征数据、标签和其他元数据封装在一个对象中，避免了在训练过程中多次传递数据，从而提高了效率。 尤其是在处理大型数据集时，使用 `Pool` 对象可以显著减少内存占用和训练时间。


__`Pool` 类的构造函数:__

`Pool` 类的构造函数接受多个参数，用于指定训练数据和元数据：

```python
class Pool(data,
           label=None,
           cat_features=None,
           text_features=None,
           embedding_features=None,
           column_description=None,
           pairs=None,
           graph=None,
           delimiter='\t',
           has_header=False,
           weight=None,
           group_id=None,
           group_weight=None,
           subgroup_id=None,
           pairs_weight=None,
           baseline=None,
           timestamp=None,
           feature_names=None,
           thread_count=-1,
           log_cout=sys.stdout,
           log_cerr=sys.stderr)
```

__参数说明:__

* __`data`__:  特征数据。可以是多种形式，例如列表、NumPy 数组、Pandas DataFrame、稀疏矩阵或文件路径。 这是必需参数。
* __`label`__:  目标变量（标签）。可以是列表或数组。
* __`cat_features`__:  类别特征的索引或名称列表。
* __`text_features`__:  文本特征的索引或名称列表。
* __`embedding_features`__:  嵌入特征的索引或名称列表。
* __`column_description`__:  列描述，用于指定特征类型等信息。
* __`pairs`__:  成对数据，用于排序任务。
* __`graph`__:  图数据，用于图神经网络。
* __`delimiter`__:  分隔符，用于从文件中读取数据。
* __`has_header`__:  布尔值，指示数据文件是否包含标题行。
* __`weight`__:  样本权重。
* __`group_id`__:  组 ID，用于分组数据。
* __`group_weight`__:  组权重。
* __`subgroup_id`__:  子组 ID。
* __`pairs_weight`__:  成对数据的权重。
* __`baseline`__:  基线预测。
* __`timestamp`__:  时间戳。
* __`feature_names`__:  特征名称列表。
* __`thread_count`__:  线程数。
* __`log_cout`__:  标准输出流。
* __`log_cerr`__:  标准错误流。


__方法:__

`Pool` 类还提供了一些方法，例如 `get_label`、`get_weight`、`get_cat_feature_indices` 等，用于访问和操作 `Pool` 对象中的数据。

`get_baseline()`：从数据集返回基线数组

`get_cat_feature_indices()`：返回在输入数据中找到的分类特征的索引

`get_embedding_feature_indices()`：返回在输入数据中找到的嵌入特征的索引。

`get_features()`：返回数据集特征的数组

`get_group_id()`：返回所有对象的组标识符数组。

`get_label()`：返回分配给输入数据的标签的值。

`get_text_feature_indices()`：返回在输入数据中找到的文本特征的索引

`get_weight()`：返回数据集中每个对象的权重列表。

`is_quantized()`：检查池是否已量化

`num_col()`：返回包含特征数据的列数

`num_row()`：返回数据集中包含的对象数量

`save(fname)`：将量化池保存到文件中

`save_quantization_borders(output_file)`：将数字特征量化中使用的边界保存到文件中。

>```python
>from catboost import Pool, CatBoostRegressor
>
>train_data = [[1, 4, 5, 6],
>    [4, 5, 6, 7],
>    [30, 40, 50, 60]]
>
>train_labels = [10, 20, 30]
>
>eval_data = [[2, 4, 6, 8],
>   [1, 4, 50, 60]]
>
>eval_labels = [20, 30]
>
>train_dataset = Pool(train_data, train_labels)
>eval_dataset = Pool(eval_data, eval_labels)
>
>train_dataset.quantize()
>train_dataset.save_quantization_borders("borders.dat")
>eval_dataset.quantize(input_borders="borders.dat")
>
>```

`set_baseline(baseline)`：为所有输入对象设置初始公式值。训练从所有输入对象的这些值开始，而不是从零开始

> ```python
> import numpy as np
> from catboost import Pool
> 
> train_data = [[76, 'blvd', 41, 50, 7],
>         [75, 'today', 57, 0, 48],
>         [70, 'letters', 33, 17, 7],
>         [72, 'now', 43, 29, 12],
>         [60, 'back', 2, 0, 1]]
> 
> label_values = [1, 0, 0, 1, 4]
> 
> input_pool = Pool(data = train_data,
>             label = label_values,
>             cat_features = [1])
> 
> input_pool.set_baseline([1, 3, 2, 1, 2])
> 
> input_pool.get_baseline()
> ```
>
> ### 基线的作用
>
> 1. **加速收敛**：通过提供初始预测值，模型可以更快地达到收敛状态。
> 2. **增量训练**：在已经训练过的模型上继续训练时，可以使用基线来保持之前的预测结果。
> 3. **模型融合**：在模型融合（ensemble）中，可以使用基线来结合多个模型的预测结果。
>
> ### 使用场景
>
> - **继续训练**：在已经训练过的模型上继续训练，使用之前的预测结果作为基线。
> - **增量学习**：在新数据上进行增量学习，使用之前的模型预测结果作为基线。
> - **模型融合**：在多个模型的预测结果基础上进行训练，使用这些预测结果作为基线。

`set_feature_names(feature_names)`：为数据集中的所有特征设置名称。

> ```python
> import numpy as np
> from catboost import Pool
> 
> train_data = [[76, 'blvd', 41, 50, 7],
>         [75, 'today', 57, 0, 48],
>         [70, 'letters', 33, 17, 7],
>         [72, 'now', 43, 29, 12],
>         [60, 'back', 2, 0, 1]]
> 
> label_values = [1, 0, 0, 1, 4]
> 
> input_pool = Pool(data = train_data,
>             label = label_values,
>             cat_features = [1])
> 
> input_pool.set_feature_names(['year', 'name', 'BLBRD', 'CAC', 'OAC'])
> ```

`set_group_id(group_id)`：为所有输入对象设置标识符。

`set_group_weight(group_weight)`：为定义组内的所有对象设置权重。

`set_pairs(pairs)`：设置成对度量的对列表

`set_pairs_weight(pairs_weight)`：为每对物体设置权重









### 量化

`Pool` 对象的 `quantize` 方法。此方法用于对 `Pool` 对象中的数值特征进行量化，即将连续数值特征转换为离散的类别特征。量化可以减少内存占用，加快模型训练速度，并可能提高模型的泛化能力。


**`quantize` 方法的用途:**

数值特征的量化是 CatBoost 训练过程中的一个重要步骤。它将连续的数值特征转换为离散的区间，每个区间代表一个类别。这使得 CatBoost 可以更有效地处理数值特征，尤其是在处理高维数据或内存受限的环境中。量化后的数据占用更少的内存，并且可以加快模型训练速度。


**`quantize` 方法的调用方式:**

`quantize` 方法是 `Pool` 对象的一个方法，其调用方式如下：

```python
pool.quantize(ignored_features=None,
              per_float_feature_quantization=None,
              border_count=None,
              max_bin=None,
              feature_border_type=None,
              dev_efb_max_buckets=None,
              nan_mode=None,
              input_borders=None,
              simple_ctr=None,
              combinations_ctr=None,
              per_feature_ctr=None,
              ctr_target_border_count=None,
              task_type=None,
              used_ram_limit=None)
```


**参数说明:**

该方法包含许多参数，用于控制量化过程的各个方面。  其中一些关键参数包括：

* **`ignored_features`**:  需要忽略的特征索引或名称列表。这些特征不会被量化。
* **`per_float_feature_quantization`**:  对指定特征进行自定义量化的设置。允许对不同的特征指定不同的量化参数。
* **`border_count` (或 `max_bin`)**:  每个数值特征要划分的区间数量。
* **`feature_border_type`**:  用于确定区间边界的算法。例如，`Uniform` 表示均匀划分，`GreedyLogSum` 表示基于贪婪算法的划分。
* **`nan_mode`**:  处理缺失值的方式。例如，`Min` 表示将缺失值视为最小值，`Max` 表示将缺失值视为最大值。


其他参数用于更精细的控制，例如处理类别特征计数器 (CTR) 的方式，以及内存限制等。


**返回值:**

`quantize` 方法直接修改 `Pool` 对象，不返回任何值。

__示例__

```python
import numpy as np
from catboost import Pool, CatBoostRegressor


train_data = np.random.randint(1, 100, size=(10000, 10))
train_labels = np.random.randint(2, size=(10000))
quantized_dataset_path = 'quantized_dataset.bin'

# save quantized dataset
train_dataset = Pool(train_data, train_labels)
train_dataset.quantize()
train_dataset.save(quantized_dataset_path)
```