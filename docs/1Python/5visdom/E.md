---
title: 🍅 PyEcharts绘图经验
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
### 3. 生成的HTML在浏览器显示空白[^1]

【问题分析】
根因：页面访问 `https://assets.pyecharts.org/assets/echarts.min.js` 受限制
【解决办法】
第一步，将上述`echarts.min.js`下载保存到本地
第二步，我这里将`echarts.min.js`使用Apache做了本地部署，获得了一个本地链接"192.168.1.7:3000/js/echarts.min.js"
第三步，项目中设置

```python
from pyecharts.globals import CurrentConfig

CurrentConfig.ONLINE_HOST = "192.168.1.7:3000/js/echarts.min.js"
```
然后生成的HTML就会指向本地地址


[^1]: cnblogs，@piecesof，[pyecharts生成HTML白页面/pyecharts指定从本地加载拉取echarts.min.js](https://www.cnblogs.com/deliaries/p/12957771.html)
