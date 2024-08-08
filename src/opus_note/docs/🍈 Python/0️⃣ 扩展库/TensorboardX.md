---
title: 🤩 TensorbordX
comments: true
---

## 壹丨安装

```bash
pip install tensorboardX
```

```bash
pip install tensorboard
```

使用GPU的情况下，需要安装：

```bash
pip install tensorflow-gpu==2.3.0
```

***注意：版本需要和cuda版本一致[^1]***

否则报`cudart64_110.dll not found`错误，可根据参考[1]查找对应版本

??? tip "查看TensorFlow版本"

	```python
	import tensorflow as tf
	print(tf.__version__)
	```


## 贰丨使用

在`runs`同级目录下执行：

```bash
tensorboard --logdir runs
```

## 叁丨总结

用法详见参考[^2][^3]，个人觉得不好用，PyTorch训练可视化可以试试`visdom` 。



[^1]: CSDN，@我想静静，，[cudart64_110.dll not found解决方法](https://blog.csdn.net/weixin_42764932/article/details/113038416)
[^2]: 简书，@苗书宇，[Pytorch使用tensorboardX可视化。超详细！！！](https://www.jianshu.com/p/46eb3004beca)
[^3]: CSDN，@imbennyguo，[详解PyTorch项目使用TensorboardX进行训练可视化](https://blog.csdn.net/bigbennyguo/article/details/87956434)
