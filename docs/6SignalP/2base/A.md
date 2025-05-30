---
title: 频谱和功率谱
date: 2024.10.20
comments: true
---

## 频谱和功率谱

### 1. 频谱（Spectrum）

__定义__：

- 频谱是信号在频域中的表示，描述了信号在不同频率成分上的幅度和相位信息。
- 频谱可以通过傅里叶变换（Fourier Transform）从时域信号中得到。

__表示__：

- 频谱通常表示为复数形式，其中实部和虚部分别表示信号的余弦和正弦成分。
- 频谱可以分为幅度谱（Magnitude Spectrum）和相位谱（Phase Spectrum）。幅度谱表示频率成分的幅度，而相位谱表示频率成分的相位。

__用途__：

- 频谱用于分析信号的频率成分，了解信号在不同频率上的分布情况。
- 在通信、音频处理、振动分析等领域中，频谱分析是常用的工具。

### 2. 功率谱（Power Spectrum）

__定义__：

- 功率谱是信号在频域中的功率分布，描述了信号在不同频率成分上的功率。
- 功率谱通常通过对频谱的幅度平方进行归一化得到。

__表示__：

- 功率谱表示为信号在每个频率成分上的功率，通常是实数形式。
- 对于离散信号，功率谱可以通过离散傅里叶变换（DFT）或快速傅里叶变换（FFT）计算得到。

__用途__：

- 功率谱用于分析信号的能量分布，了解信号在不同频率上的能量贡献。
- 在信号处理、通信、雷达、地震学等领域中，功率谱分析是常用的工具。

__计算__：

1. __Welch方法__：由于分段、加窗和平均的过程，Welch方法计算的功率谱密度通常更加平滑，噪声影响较小。
2. __直接使用FFT__：直接使用FFT计算的功率谱可能会受到单次FFT计算中的随机噪声影响，结果可能不如Welch方法平滑。

### 3. 数学表示

假设 $x(t)$ 是一个时域信号，其傅里叶变换为 $X(f)$，则：

- __频谱__ $X(f)$ 是信号 $x(t)$ 在频域中的表示，包含幅度和相位信息。

- __功率谱__ $P(f)$ 是频谱 $X(f)$ 的幅度平方，即：


$$
P(f) = |X(f)|^2
$$


### 示例

```python
import numpy as np
import matplotlib.pyplot as plt

# 生成示例信号
fs = 1000  # 采样频率
t = np.arange(0, 1, 1/fs)  # 时间向量
f1, f2 = 50, 120  # 信号频率
x = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)  # 生成信号

# 计算频谱
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(len(X), 1/fs)

# 计算功率谱
P = np.abs(X)**2 / len(X)

# 绘制频谱和功率谱
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(frequencies[:len(frequencies)//2], np.abs(X)[:len(X)//2])
plt.title('频谱')
plt.xlabel('频率 (Hz)')
plt.ylabel('幅度')

plt.subplot(2, 1, 2)
plt.plot(frequencies[:len(frequencies)//2], P[:len(P)//2])
plt.title('功率谱')
plt.xlabel('频率 (Hz)')
plt.ylabel('功率')

plt.tight_layout()
plt.show()
```

![频谱](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/%E9%A2%91%E8%B0%B1.webp)
