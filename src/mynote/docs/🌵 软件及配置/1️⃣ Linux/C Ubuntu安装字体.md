---
title: 🍎 Ubuntu安装字体
date: 2023.10.13
comments: true
---

### 第一步，复制字体

将字体文件复制到`~/.fonts/`文件夹下。这个文件夹是用于存储个人用户的字体文件的，如果该文件夹不存在，可以通过以下命令创建：

```bash
mkdir ~/.fonts
```

然后将字体文件复制到该文件夹下，例如：

```bash
cp /path/to/font.ttf ~/.fonts/
```

### 第二步，刷新字体缓存

复制完成后，可以在终端中运行以下命令使字体生效：

```bash
fc-cache -f -v
```

这个命令会重新建立字体缓存，使新安装的字体能够被系统识别和使用。

??? tip "查看所有字体"

    ```bash
    fc-list
    ```

### 第三步，Matplotlib刷新字体缓存【可选】

Ubuntu的Matplotlib刷新字体缓存

```python
import matplotlib
print(matplotlib.get_cachedir())
```

我的是`/home/MasterMao/.cache/matplotlib`

删掉这个文件夹下的`fontlist-v330.json`，再次使用`matplotlib`时会自动刷新字体缓存

