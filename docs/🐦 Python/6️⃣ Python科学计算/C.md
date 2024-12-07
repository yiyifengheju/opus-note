---
title: 🥣 Scipy
comments: true
---

## 壹丨Scipy库

简介：Scipy是一个开源的Python算法库和数学工具包，包含的模块有最优化、线性代数、积分、插值、特殊函数、快速傅里叶变换、信号处理和图像处理、常微分方程求解和其他科学与工程中常用的计算[^1]。

官网：[SciPy](https://scipy.org/)

安装：`pip install scipy`

## 贰丨应用

### 1.寻找离散序列极值点[^2]

```python
scipy.signal.argrelmax()
scipy.signal.argrelmin()
```

??? note "代码"

    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.signal as signal
    import scienceplots
    
    plt.style.use('mastermao-simtimes')


    def run():
        time_series = np.array([0, 6, 25, 20, 15, 8, 15, 6, 0, 6, 0, -5, -15, -3, 4, 10, 8, 13, 8, 10, 3, 1, 20, 7, 3, 0])
        max_list = signal.argrelmax(time_series)[0]
        min_list = signal.argrelmin(time_series)[0]
    
        figure, axes = plt.subplots(figsize=(7.05, 2.35))
        axes.plot(time_series)
        axes.scatter(max_list, time_series[max_list], label='极大值点')
        axes.scatter(min_list, time_series[min_list], label='极小值点')
        axes.legend(loc='upper right')
        plt.savefig('./极大极小值示例.webp')
        plt.show()


    if __name__ == '__main__':
        run()
    ```

![极大极小值示例](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/极大极小值示例.webp)



!!! warning "当极值点左右值相等时无法识别"

### 2. 重采样

函数：[`scipy.signal.resample`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.resample.html#scipy.signal.resample)

```python
scipy.signal.resample(x, num, t=None, axis=0, window=None, domain='time')
```




[^1]: @维基百科，[SciPy](https://zh.wikipedia.org/wiki/SciPy)
[^2]: @灰信网，[python寻找离散序列极值点](https://www.freesion.com/article/6333281915/)
