---
title: 🥰 SciencePlots
comments: true
---

SciencePlots是一个基于Matplotlib的Python科学绘图库，它旨在为科学家和工程师提供高质量的绘图工具。它提供了一些常用的绘图类型，如线图、散点图、直方图、热力图、等高线图等，并支持自定义颜色、线型、标签和图例等。此外，它还提供了一些可用于美化绘图的实用程序，如调整字体、线宽和标签大小等。

安装：`pip install SciencePlots`

开源地址：https://github.com/garrettj403/SciencePlots

## 壹丨简单使用

!!! warning "注意"

	在2.0.0版本后，需要添加`import scienceplots`才能使用`plt.style.use('science')`

!!! note "Ubuntu下SciencePlots样式设置"

	将样式文件复制到：/home/$user_name$/anaconda3/envs/MasterMaoPy311/lib/python3.11/site-packages/scienceplots/styles/misc/

!!! note "参考SciencePlots样式(中文宋体+英文TimesNewRoman)"
	
	合并方法：[毕业论文 Matplotlib 绘图中英文设置（二）](https://www.mastermao.cn/2022/%E6%AF%95%E4%B8%9A%E8%AE%BA%E6%96%87Matplotlib%E7%BB%98%E5%9B%BE%E4%B8%AD%E8%8B%B1%E6%96%87%E8%AE%BE%E7%BD%AE%EF%BC%88%E4%BA%8C%EF%BC%89/)
	
	样式代码：
	```yaml
	# Matplotlib style for scientific plotting
	# This is the base style for "SciencePlots"
	# see: https://github.com/garrettj403/SciencePlots
	
	# Set default figure size
	figure.figsize : 3.5, 2.625
	figure.dpi : 600
	
	# Set x axis
	xtick.direction : in
	xtick.major.size : 3
	xtick.major.width : 0.5
	xtick.minor.size : 1.5
	xtick.minor.width : 0.5
	xtick.minor.visible : True
	xtick.top : True
	xtick.labelsize : medium
	
	# Set y axis
	ytick.direction : in
	ytick.major.size : 3
	ytick.major.width : 0.5
	ytick.minor.size : 1.5
	ytick.minor.width : 0.5
	ytick.minor.visible : True
	ytick.right : True
	ytick.labelsize : medium
	
	axes.unicode_minus : False
	
	# Set line widths
	axes.linewidth : 0.5
	grid.linewidth : 0.5
	lines.linewidth : 1.
	lines.markersize : 4.0
	
	# Set line style as well for black and white graphs
	axes.prop_cycle : (cycler('color', ['k', 'r', 'b', 'g']) + cycler('ls', ['-', '--', ':', '-.']))
	
	# save config
	savefig.bbox : tight
	savefig.format : webp
	savefig.dpi : 600
	savefig.pad_inches : 0.05
	
	# Grid lines
	axes.grid : True
	axes.axisbelow : True
	grid.linestyle : --
	grid.color : k
	grid.alpha : 0.2
	
	# Legend
	legend.frameon : True
	legend.framealpha : 1.0
	legend.fancybox : True
	legend.numpoints : 1
	axes.labelsize : 7
	legend.fontsize : 7
	
	# Use serif fonts
	font.size : 7
	font.serif : Times New Roman + SimSun
	font.family : serif
	
	# Use LaTeX for math formatting
	text.usetex : False
	```
	​## 贰丨实例

下面是一个简单的例子：

```python
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('mastermao-simtimes')


def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))


if __name__ == '__main__':
    x = np.linspace(0.75, 1.25, 201)

    fig, ax = plt.subplots(figsize=(7.05, 3), constrained_layout=True)
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.set(xlabel=r'电压 (mV)')
    ax.set(ylabel=r'电流 ($\mu$A)')
    ax.autoscale(tight=True)
    fig.savefig('./fig.webp')

```

![fig](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/fig.webp)