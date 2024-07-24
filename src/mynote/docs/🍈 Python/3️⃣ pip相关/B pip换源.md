---
title: 🛁 pip换源
comments: true
---


经常遇到pip安装慢的问题，解决方法就是换源。国内镜像源包括但不限于[^1]：

```bash
# 清华镜像站
https://pypi.tuna.tsinghua.edu.cn/simple
# 中科大镜像站
https://pypi.mirrors.ustc.edu.cn/simple/
# 豆瓣镜像站
http://pypi.douban.com/simple/
# 阿里云
http://mirrors.aliyun.com/pypi/simple/
```

### 方法1：临时指定镜像地址

`pip`命令中添加`-i`参数，如：

```bash
pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 方法2：PyCharm中添加国内镜像站

第一步，PyCharm——File——Settings——定位到工程“Project：xxxx”——Project Interpreter——点击加号

第二步，点击Manage Repositories

第三步，添加镜像源

<div class="inline-img">
<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20220104013154363.png" alt="image-20220104013154363" >
<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20220104013242169.png" alt="image-20220104013242169" >
</div>

### 方法3：全局pip配置（推荐）[^2]

Windows下，新建文件：`C:\Users\MasterMao\pip\pip.ini`，以清华镜像源为例：

```bash
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```

Linux/MacOS下，新建文件并编辑 `~/.pip/pip.conf`：

```bash
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```





[^1]: RUNOOB.COM，[pip 使用国内镜像源](https://www.runoob.com/w3cnote/pip-cn-mirror.html)
[^2]: CSDN, @魏有心，[PyCharm解决安装慢的问题 更换pip源为国内源](https://blog.csdn.net/weixin_43954778/article/details/89821988)
