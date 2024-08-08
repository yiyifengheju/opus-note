---
title: A 相位差计算
comments: true
---

## 壹丨问题分析

两条时间序列存在一定的相位差，怎样提取它们之间的相位差呢？

* 使用移动平移相关性TLCC，补偿相移再计算
* 使用Scipy封装的函数实现

## 贰丨Scipy提取相位差

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

plt.style.use('mastermao-simtimes')


def get_diff(x, y):
    correlation = signal.correlate(x, y, mode="full")
    lags = signal.correlation_lags(x.size, y.size, mode="full")
    delay = lags[np.argmax(correlation)]
    return delay


def plot_delay(x, y, delay):
    signal_shifted = np.roll(y, int(delay))

    fig, ax = plt.subplots(figsize=(7.05, 3), constrained_layout=True)
    ax.plot(x, label='参考信号')
    ax.plot(y, label='实际信号')
    ax.plot(signal_shifted, label='补偿相移信号')
    x_lim, y_lim = ax.get_xlim(), ax.get_ylim()
    # ax.text(x=x_lim[1] - 0.1, y=y_lim[1] - 0.1, s=f'Delay = {delay:.2f}', ha='right', va='top')
    ax.legend(loc='upper right', title=f'Delay = {delay:.2f}')
    plt.savefig(f'./ps.webp')
    plt.show()


if __name__ == '__main__':
    # 采样频率
    fs = 125

    # 参考信号和待测信号的采样数据
    x = np.sin(np.arange(0, 3000) / fs)
    y = 0.8 * np.sin(np.arange(0, 3000) / fs + 5)

    delay = get_diff(x, y)
    plot_delay(x, y, delay)

```



![ps](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/ps.webp)





