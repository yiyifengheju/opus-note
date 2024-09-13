---
title: 🐎️ 视频截取图片
date: 2022-05-29
comments: true
---

## 问题描述：

> 做毕业设计遇到的问题：

1. 训练多种气体回归模型。为了简化代码，数据导入、绘图等已经封装成函数，通过传递气体名称调用即可，但这就需要手动修改气体名，每种气体都要单独训练一次，懒得每次训练完从床上爬起来改俩参数重新训练！！
2. 目标检测模型自动标注。已经使用小批量数据训练模型，下一步即使用模型做自动标注，但图片数据有2w张！理论上图片检测都是秒出结果（Dr.Ma的2080s加持），但在检测到几千张后明显跑不动了，目测程序边检测边吃内存……

## 尝试：

> 尝试一：添加`for`循环，遍历气体名称

会爆内存，训练到第二个模型时电脑就开始卡，且每步训练时间很长

> 尝试二：训练完一组后，释放内存

学艺不精，似乎好像也许大概maybe，Python没法手动回收内存



## 最终解决方案：

> 使用`argparse`模块和`os.system()`方法

### 针对问题一：训练多种气体回归模型

第一步丨调用`argparse`

```python
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gas', type=str, default='funan', help='气体类型')
    arg = parser.parse_args()
    print(f'Starting Analysis: {arg.gas}!')
    run(arg.gas)
```



第二步丨格式化 `run()` 函数

除了正常传递参数外，使用格式化语句和字典变量，如：

```python
# 格式化语句
train_data_path = f'./regression_data/{gas_name}/train/'

# 字典变量
gas_name_dict = {'funan':'呋喃'}
legend_title = f'{gas_name_dict[gas_name]}-模型测试'
ax.legend(titile='legend_title')
```



第三步丨编写自动化脚本

新建 `auto_run.py` ，使用 `os.system()`函数，搭配自定义命令行参数，实现自动运行

```python
import os

if __name__ == "__main__":
    gas_list = ['funan', ...]
    for gas in gas_list:
        os.system(f'python cnn_regression.py --gas {gas}')
```

***目测可以达到期望效果***，运行中没有卡顿出现，内存占用9.3GB/16GB（所用CNN参数量很小）



### 针对问题二：目标检测模型自动标注

观察YOLOv5检测程序`detect.py`，关键参数：

```python
parser.add_argument('--weights', nargs='+', type=str, default=ROOT / 'xxxx.pt', help='model path(s)')
parser.add_argument('--source', type=str, default=ROOT / 'xx/xxx', help='file/dir/URL/glob, 0 for webcam')
```

其中，`--weights`参数传入模型文件地址；`--source`参数传入图片地址



第一步，对2w张图片划分为小批量

```python
import os
import tqdm
import shutil


def run():
    pic_path = './images'
    pic_dict = os.listdir(pic_path)
    for i in range(1, 21):
        if not os.path.exists(f'./batch{i}'):
            os.mkdir(f'./batch{i}')
        for item in tqdm.tqdm(pic_dict[1000 * (i - 1):1000 * i]):
            shutil.move(os.path.join(pic_path, item), os.path.join(f'./batch{i}', item))


if __name__ == '__main__':
    run()
```

以1000张为一组，划分为20组，如果有随机打乱的需求可以加入：

```python
import random
random.shuffle(pic_dict)
```



第二步，编写自动化脚本

```python
import os

if __name__ == "__main__":
    for idx in range(1, 22):
        os.system(f'python auto_label_detect.py --source xxxx/batch{idx}')
```

当然，如果有睡眠需求，可以加入：

```python
os.system('shutdown -s -t 60')
```

其中，`-t 60`为60秒后自动关机，确保系统文件保存，建议不要立刻关机



## 参考

> [1] 博客园，@倥偬时光，[python基础之os.system函数](https://www.cnblogs.com/cwp-bg/p/8465566.html)
> [2] 博客园，@苍青浪，[调用系统命令 os.system()和os.popen()]( https://www.cnblogs.com/cangqinglang/p/12190939.html)
> [3] 博客园，@一一风和橘，[Python argparse模块](https://www.cnblogs.com/mastermao/p/15956913.html)
> [4] [Python官方文档](https://docs.python.org/zh-cn/3/library/argparse.html)