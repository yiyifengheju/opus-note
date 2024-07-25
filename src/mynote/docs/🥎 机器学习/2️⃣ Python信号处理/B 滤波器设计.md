---
title: B 滤波器设计
comments: true
---



TODO



### 1. 带通滤波：

```python
def sos_bandpass(in_signal, low_cut, high_cut, freq=100, order=4):
    """
    对输入信号进行带通滤波
    
    :param in_signal: 1d array，输入信号
    :param low_cut: float，滤波器下截止频率(Hz)
    :param high_cut: float，滤波器上截止频率(Hz)
    :param freq: int or float，输入信号采样率(Hz)
    :param order: int，滤波器阶数
    :return: 1d array，滤波后参数
    """
    nyquist_freq = 0.5 * freq
    low = low_cut / nyquist_freq
    high = high_cut / nyquist_freq
    sos = signal.butter(order, [low, high], btype='bandpass', output='sos')
    out_signal = signal.sosfiltfilt(sos, in_signal)
    return out_signal
```



### 2. 高通滤波

```python
def sos_highpass(in_signal, low_cut, freq=100, order=4):
    """
    对输入信号进行高通滤波
    :param in_signal: 1d array，输入信号
    :param low_cut: float，滤波器下截止频率(Hz)
    :param freq: int or float，输入信号采样率(Hz)
    :param order: int，滤波器阶数
    :return: 1d array，滤波后参数
    """
    nyquist_freq = 0.5 * freq
    low = low_cut / nyquist_freq
    sos = signal.butter(order, low, btype='high', output='sos')
    out_signal = signal.sosfiltfilt(sos, in_signal)
    return out_signal
```



### 3. 低通滤波

```python
def sos_lowpass(in_signal, high_cut, freq=100, order=4):
    """
    对输入信号进行高通滤波
    :param in_signal: 1d array，输入信号
    :param high_cut: float，滤波器上截止频率(Hz)
    :param freq: int or float，输入信号采样率(Hz)
    :param order: int，滤波器阶数
    :return: 1d array，滤波后参数
    """
    nyquist_freq = 0.5 * freq
    high = high_cut / nyquist_freq
    sos = signal.butter(order, high, btype='low', output='sos')
    out_signal = signal.sosfiltfilt(sos, in_signal)
    return out_signal
```





































