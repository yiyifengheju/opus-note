---
title: PyEcharts绘图经验
comments: true
---

### 1. 绘图曲线不显示

使用的数据类型不能是`np.ndarray`，如：

```python
line.add_xaxis(xaxis_data=data.index.to_list())
```

解决方法：最好使用`pandas.DataFrame`数组

### 2. 曲线结尾连到前面数据

解决方法：在绘图数据结尾添加`None`，如：

```python
y_data = data[col].values.tolist()
y_data.append(None)
```

