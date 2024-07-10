---
title: J wget代理设置
comments: true
---


如下显示可能是被公司内网墙掉了，需要设置代理

```bash
Connecting to physionet.org (physionet.org)|18.18.42.54|:443... failed: Resource temporarily unavailable.
Retrying.
```

## 壹丨代理设置

### 1. 推荐配置

Ubuntu下修改`~/.wgetrc`文件，Windows用户目录下修改或新建`.wgetrc`，添加：

```ini
http_proxy = http://example.com:8080
https_proxy = https://example.com:8080
proxy_user = USER_NAME
proxy_password = PASSWORD
use_proxy = on
wait = 15
```

> *注意：密码中的特殊字符需要用编码替代*
>
> | 特殊字符 | 编码 | 特殊字符 | 编码 | 特殊字符 | 编码 |
> | -------- | ---- | -------- | ---- | -------- | ---- |
> | !        | %21  | &        | %26  | )        | %29  |
> | #        | %23  | '        | %27  | *        | %2A  |
> | $        | %24  | (        | %28  | +        | %2B  |
> | ,        | %2C  | /        | %2F  | :        | %3A  |
> | ;        | %3B  | =        | %3D  | ?        | %3F  |
> | @        | %40  | [        | %5B  | ]        | %5D  |

### 2. 临时配置

临时使用proxy，可以使用：

```bash
export http_proxy=http://USER_NAME:PASSWORD@example.com:8080
export https_proxy=https://USER_NAME:PASSWORD@example.com:8080
```

## 贰丨解决方案

### 1. Windows解决方案

Windows系统下`wget`命令不可用，下面给出一种曲线救国的方法：

第一步，下载`wget.exe`，网址：[GNU Wget 1.21.4 for Windows (eternallybored.org)](https://eternallybored.org/misc/wget/)

第二步，放在用户目录下：`C:\Users\username`

第三步，配置代理。在用户目录下新建`.wgetrc`文件，添加代理配置：

```ini
http_proxy = http://example.com:8080
https_proxy = https://example.com:8080
proxy_user = USER_NAME
proxy_password = PASSWORD
use_proxy = on
wait = 15
```

第四步，目标文件夹下新建`scripts.py`：

```python
import os

cmd = 'C:\\Users\\username\\wget.exe -r -N -c -np https://physionet.org/files/mimic3wdb-matched/1.0/'
os.system(cmd)
```

### 2. Linux解决方案

可以搜索使用`mwget`替代`wget`，可以实现多线程下载。