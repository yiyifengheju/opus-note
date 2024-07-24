---
title: C Matplotlib中英文设置（一）
comments: true
---


## 壹丨Matplotlib无法同时使用两种字体

毕设论文绘图要求中文宋体、英文新罗马，但使用Matplotlib绘图时无法同时使用两种字体。例如：

```python
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 15}
plt.legend(prop=font)
```

> 上述代码设置图例字体为新罗马，但当图例中出现CJK字符时会变成方块。


!!! note "解决思路"

	1. 参考[^1]使用华文宋体接近“SimSun+Times New Roman”的效果。
	2. 不要求中文宋体、英文新罗马时，可以使用Noto Serif SC字体，可以避免中文变成小方块。
	3. 本文使用pgf输出符合毕设条件的绘图

## 贰丨解决方法[^2]

第一步，安装LaTeX软件，Windows推荐[MiKTex](https://miktex.org/)，macOS推荐[MacTeX](https://www.tug.org/mactex/)。

第二步，新建绘图样式于：`C:\Users\MasterMao\.matplotlib\stylelib\mastermao.mplstyle` 

```yaml
# 多颜色循环
axes.prop_cycle : (cycler('color', ['black', 'r', 'g', 'b', '#e08c00', '#1bd38b', '#8290ff', '#394b41', '#9cb0a4', '#00d0ff', '#0099e0']) + cycler('ls', ['-', '--', ':', '-.']))
# 少颜色循环
axes.prop_cycle : (cycler('color', ['k', 'r', 'b', 'g']) + cycler('ls', ['-', '--', ':', '-.']))

# 默认图片大小、分辨率
figure.figsize : 3.5, 2.625
figure.dpi : 1200

# x轴设置
xtick.direction : in
xtick.major.size : 3
xtick.major.width : 0.5
xtick.minor.size : 1.5
xtick.minor.width : 0.5
xtick.minor.visible : True
xtick.top : True
xtick.labelsize : medium

# y轴设置
ytick.direction : in
ytick.major.size : 3
ytick.major.width : 0.5
ytick.minor.size : 1.5
ytick.minor.width : 0.5
ytick.minor.visible : True
ytick.right : True
ytick.labelsize : medium # xx-small, x-small, small, medium, large, x-large, xx-large, smaller, larger.

# 正常显示负号
axes.unicode_minus : False

# 设置线宽
axes.linewidth : 0.5
grid.linewidth : 0.5
lines.linewidth : 1.
lines.markersize : 4.0

# 紧凑视图
savefig.bbox : tight
savefig.pad_inches : 0.05

# 设置衬线字体，公式使用stix字体（非常接近新罗马）：
font.size : 7
font.family : serif
mathtext.fontset : stix

# 设置LaTeX渲染文本：
text.usetex : True
pgf.rcfonts : False
pgf.preamble : \usepackage{unicode-math} \setmainfont{Times New Roman} \usepackage{xeCJK} \xeCJKsetup{CJKmath=true} \setCJKmainfont{SimSun}
```

## 叁丨测试用例

使用示例：

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


# 使用pgf渲染，绘图样式选择 `mastermao.mplstyle`
mpl.use("pgf")
plt.style.use(['mastermao'])

def run():
    data = pd.DataFrame({'Decision Tree': [95, 75], 'SVM': [92, 67], 'MLP': [99, 87]})
    x_label = ['A数据集', 'B数据集']

	# 生成子图
    fig, axes = plt.subplots(figsize=(4, 2.5))
    data.plot(kind='bar', stacked=False, ax=axes, width=0.3)
    plt.plot(range(2), [95.33, 76.33], marker='d', color='orangered', label='平均', markersize=4, linestyle='-.')
    plt.ylabel(r'准确率/%')
    # 限定y轴范围
    plt.ylim((65, 100))
    # 替换x轴标签，设定旋转角度
    plt.xticks(range(2), x_label, rotation=0)
    # 设置图例位置、微调位置、图例分几列、标题……
    plt.legend(frameon=True, loc="upper right", bbox_to_anchor=(1, 1), ncol=1, title="", shadow=False, fancybox=False)
	# 保存绘图
    plt.savefig(f'./img/fig2-30.png', format='png', bbox_inches='tight', transparent=True, dpi=1200)
    plt.savefig(f'./img/fig2-30.pdf', format='pdf', bbox_inches='tight', transparent=True, dpi=1200)

if __name__ == '__main__':
    run()
```



## 附丨无SimSun、Times要求时使用Noto Serif SC字体[^3]

不要求中文宋体、英文新罗马时，可以使用包含中英文字符的字体，这里使用Google的[Noto Serif SC字体](https://fonts.google.com/noto/specimen/Noto+Serif+SC?noto.query=noto&noto.region=CN)（旧版叫Noto Serif CJK SC）

下载安装字体后，删除`用户/.matplotlib/fontlist-v330.json`，稍后使用时会重新生成



[^1]: 知乎，@如果我可以忘记，[回复“用Python的matplotlib画图，怎么保证xlabel中中文用宋体，英文用新罗马？”](https://www.zhihu.com/question/344490568/answer/936561524?utm_source=wechat_session)
[^2]: 知乎，@cherichy，[Matplotlib 中英文及公式字体设置](https://zhuanlan.zhihu.com/p/118601703)
[^3]: GitHub，@John D. Garrett，[garrettj403/SciencePlots](https://github.com/garrettj403/SciencePlots)
