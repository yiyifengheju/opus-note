---
title: 🍎 Matplotlib绘图
comments: true
---



### 1. Bland-Altman图

Bland-Altman图是一种用于比较两种测量方法或两个观察者之间一致性的图表。它可以帮助我们判断两种测量方法或两个观察者之间是否存在定量偏差或系统性误差，以及它们之间的随机误差大小和分布情况[^1]。

??? tip "查看代码"
	
    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    
    from PyAqua import config
    
    config.plt_style()


    def plot_bland_altman(true, pred, title='', save_path=''):
        true = np.asarray(true)
        pred = np.asarray(pred)
        mean = np.mean([true, pred], axis=0)
        diff = true - pred
        md = np.mean(diff)
        sd = np.std(diff, ddof=1)
    
        figure, ax = plt.subplots(figsize=(7.05, 3), constrained_layout=True)
        ax.scatter(mean, diff, color='blue')
        ax.axhline(md, color='gray', linestyle='-')
        x_lim = ax.get_xlim()
        ax.text(x=x_lim[1] * 0.98, y=md * 1.1, s=f'Mean Diff: {md:.2f}', ha='right', va='bottom')
        ax.axhline(md + 1.96 * sd, color='gray', linestyle='--')
        ax.text(x=x_lim[1] * 0.98, y=(md + 1.96 * sd) * 0.95, s=f'+1.96 SD: {md + 1.96 * sd:.2f}', ha='right', va='top')
        ax.axhline(md - 1.96 * sd, color='gray', linestyle='--')
        ax.text(x=x_lim[1] * 0.98, y=(md - 1.96 * sd) * 0.95, s=f'-1.96 SD: {md - 1.96 * sd:.2f}', ha='right', va='bottom')
    
        ax.set(title='Bland Altman Plot',
               xlabel='Means',
               ylabel='Difference')
        plt.savefig(f'{save_path}/{title}.webp')
        plt.close()
    
    if __name__ == '__main__':
        PATH_FIGURE = '../Figure'
    
        a = np.random.random(100) * 100
        b = a + (np.random.random(100) - 0.5) * 10
        plot_bland_altman(a, b, title='Bland_Altman', save_path=PATH_FIGURE)
    ```
    
    ![Bland_Altman](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311112321603.webp)

### 2.  Pearson相关性图

皮尔逊相关系数图是一种用于展示两个变量之间线性关系的图表，它可以帮助我们评估两个变量之间的相关性强度和方向，即它们之间的正相关、负相关或无相关关系。

??? tip "查看代码"
    
    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    
    from PyAqua import config
    
    config.plt_style()


    def __pearsonr_line(x, b, k):
        return k * x + b


    def plot_pearsonr(true, pred, title='', save_path=''):
        from scipy import stats
    
        true = np.asarray(true)
        pred = np.asarray(pred)
        trend, intercept, rsq1, p_value, std_err = stats.linregress(true, pred)
        cc = stats.pearsonr(true, pred)
        if cc[1] < 0.001:
            p = 'P<0.001'
        elif cc[1] < 0.01:
            p = 'P<0.01'
        elif cc[1] < 0.05:
            p = 'P<0.05'
        else:
            p = ''
    
        figure, ax = plt.subplots(figsize=(7.05, 3), constrained_layout=True)
        ax.scatter(true, pred, color='g')
        ax.plot(true, __pearsonr_line(true, intercept, trend), label=f"R = {cc[0]:.4f}, {p}")
        ax.set(title=f'{title}',
               xlabel=f'True',
               ylabel=f'Predict')
        ax.legend(loc='upper right')
        plt.savefig(f'{save_path}/{title}-Pearsonr.webp')
        plt.close()


    if __name__ == '__main__':
        PATH_FIGURE = '../Figure'
    
        a = np.random.random(100) * 100
        b = a + (np.random.random(100) - 0.5) * 10
        plot_pearsonr(a, b, title='Pearsonr', save_path=PATH_FIGURE)
    ```

![Pearsonr-Pearsonr](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311112329218.webp)


### 3. 快速傅立叶变换

使用快速傅里叶变换（FFT）将信号转换为频谱图，以理解信号的频率分布

??? tip "查看代码"
	
    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.fftpack import fft
    
    from PyAqua import config
    
    config.plt_style()


    def plot_fft(signal, sample_rate, fq_limit=None, title='', save_path=''):
        ppg_fft = np.asarray(fft(signal))
    
        fig, ax = plt.subplots(2, 1, figsize=(7.05, 3), constrained_layout=True)
        x = np.arange(len(signal)) / sample_rate
        ax[0].plot(x, signal)
        ax[0].set(title='Raw')
    
        x = np.arange(len(ppg_fft)) * sample_rate / len(ppg_fft)
        ax[1].plot(x[1:int(len(x) / 2)], np.abs(ppg_fft)[1:int(len(x) / 2)])
        ax[1].set(title='FFT',
                  xlabel='Frequency (Hz)',
                  ylabel='Amplitude')
        if fq_limit is not None:
            ax[1].set(xlim=fq_limit)
    
        plt.savefig(f'{save_path}/{title}.webp')
        plt.close()
    
    def __fake_signal(sample_rate, seconds):
        # 生成随机频率和振幅
        freq = np.random.uniform(0.5, 2.5, 100)
        amplitude = np.random.uniform(0.5, 1.5, 100)
    
        # 定义时间轴
    
        time = np.linspace(0, seconds, seconds * sample_rate)
    
        # 计算信号
        signal = np.zeros_like(time)
        for i in range(100):
            signal += amplitude[i] * np.sin(2 * np.pi * freq[i] * time)
    
        return signal
    
    if __name__ == '__main__':
        PATH_FIGURE = '../Figure'
        sig = __fake_signal(sample_rate=500, seconds=10)
        plot_fft(sig, sample_rate=500, fq_limit=(0, 20), title='FFT', save_path=PATH_FIGURE)
    ```

![FFT](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311120012222.webp)


### 4. 柱状图

??? tip "查看代码"
	
    ```python
    import matplotlib.pyplot as plt
    
    from PyAqua import config
    
    config.plt_style()


    def plot_bar(data, label,
                 ylim=None,
                 title='',
                 save_path=''):
        fig, ax = plt.subplots(figsize=(7.05, 3), constrained_layout=True)
        x = list(range(len(data)))
        ax.bar(x, data)
        for idx in x:
            ax.text(x=idx, y=data[idx] * 1.05, s=f'{data[idx]:.2f}%', ha='center', va='bottom')
        ax.set(title=f'{title}')
        if ylim is not None:
            ax.set(ylim=ylim)
        ax.set_xticks(x, label)
        plt.savefig(f'{save_path}/{title}_Bar.webp')
        plt.close()


    if __name__ == '__main__':
        PATH_FIGURE = '../Figure'
        a = [27.26889058, 22.96422388, 26.00080221, 14.82282119, 0., 3.92095272, 5.02230942]
        label = ['你', '好', '今', '天', '星', '期', '四']
        plot_bar(a, label, ylim=(0, 50), title='特征贡献率', save_path=PATH_FIGURE)
    ```

![特征贡献率_Bar](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311120020578.webp)

### 5. 直方图（Matplotlib）

直方图可以帮助我们了解数据的中心趋势、离散程度和分布形状，是数据分析中常用的工具之一。

??? tip "查看代码"
	
    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    
    from PyAqua import config
    
    config.plt_style()


    def plot_hist(data, bins=50, title='', save_path=''):
        fig, ax = plt.subplots(figsize=(7.05, 3), constrained_layout=True)
        ax.hist(data, bins=bins, alpha=0.5, rwidth=0.9)
        ax.set(title=f'{title}分布')
        plt.savefig(f'{save_path}/{title}-Hist.webp')
        plt.close()


    if __name__ == '__main__':
        PATH_FIGURE = '../Figure'
        points = np.random.normal(size=4000)
        plot_hist(points, bins=100, title='随机点', save_path=PATH_FIGURE)
    ```

![随机点-Hist](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311120026572.webp)

### 6. 直方图（Seaborn）

??? tip "查看代码"
	
    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    
    from PyAqua import config
    
    config.plt_style()


    def plot_hist_seaborn(data, bins=50, title='', save_path=''):
        fig, ax = plt.subplots(figsize=(7.05, 3), constrained_layout=True)
        sns.histplot(data=data, kde=True, ax=ax, bins=bins, legend=False)
        ax.set(title=f'{title}分布',
               ylabel='计数')
        plt.savefig(f'{save_path}/{title}-Hist-Seaborn.webp')
        plt.close()


    if __name__ == '__main__':
        PATH_FIGURE = '../Figure'
        points = np.random.normal(size=4000)
        plot_hist_seaborn(points, bins=100, title='随机点', save_path=PATH_FIGURE)
    ```

![随机点-Hist-Seaborn](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311120032360.webp)

### 7. 误差棒

误差棒（error bar）是一种用于展示数据误差范围的图形符号，它可以显示数据的方差、标准差、标准误差、置信区间或其它误差度量。误差棒可以帮助我们评估实验或观察数据的可靠性和精度，以及比较不同数据组之间的差异和相似性。[^2]

??? tip "查看代码"
	
    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    
    from PyAqua import config
    
    config.plt_style()


    def plot_error_bar(data, xlabel=None, ylim=None, title='Default_Error_Bar', save_path=''):
        data = np.asarray(data)
        length = len(data[:, 0])
        x = np.arange(length)
    
        fig, ax = plt.subplots(figsize=(7.05, 3), constrained_layout=True)
        ax.plot(data[:, 0])
        # 误差棒
        ax.errorbar(x, data[:, 0], data[:, 1],
                    ecolor='k', elinewidth=0.5, marker='s', mfc='orange', mec='k',
                    mew=1, ms=10, alpha=1, capsize=5, capthick=3, linestyle="none", label="Observation")
        # 文本标记
        for i in range(length):
            ax.text(x=i + 0.3, y=data[i, 0], s=f'{data[i, 0]}', color='blue')
        # 替换横坐标
        if xlabel is not None:
            ax.set_xticks(x, xlabel)
        if ylim is not None:
            ax.set(ylim=ylim)
        ax.set(title=title)
        if save_path:
            plt.savefig(f'{save_path}/{title}.webp')
            plt.close()
        else:
            return ax


    if __name__ == '__main__':
        PATH_FIGURE = '../Figure'
        mean = np.random.randint(5, 10, size=20) / 10
        std = np.random.randint(5, 10, size=20) / 100
        in_data = np.c_[mean, std]
        plot_error_bar(in_data, title='Error Bar', save_path=PATH_FIGURE)
    ```

![Error Bar](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/202311121200416.webp)


[^1]: CSDN，@MasterQKK被注册，[Python_基于statsmodel包画Bland altman plot （Mean Difference Plot）用于预测结果分析](https://blog.csdn.net/QKK612501/article/details/116013212) ↩

[^2]: 脚本之家，@喜马拉雅的夜空，[Python中使用matplotlib模块errorbar函数绘制误差棒图实例代码](https://www.jb51.net/article/260297.htm) ↩