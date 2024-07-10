---
title: H Pycharm创建requirements
comments: true
---

!!! note "安装依赖包命令"

    ```bash
    pip install -r requirements.txt
    ```

### 第一种：针对单虚拟环境

```bash
pip freeze > requirements.txt
```

生成的requirements.txt文件仅包括 ***当前虚拟环境*** 的依赖包和对应版本号



### 第二种：针对全局环境

```bash
pip install pipreqs
```

```bash
pipreqs . --encoding=utf8 --force
```

生成的requirements.txt文件包括 ***全局环境*** 的依赖包和对应版本号



### 第三种：使用Pycharm

对于已经完善的项目来说，直接限定版本号的方法可以保证项目迁移后的正常运行。但个人使用过程中往往不需要限定版本号，可以使用PyCharm自带的功能实现。

TooLs——Sync Python Requirements...

<img src="https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20220506064334394.png" width=60% />
