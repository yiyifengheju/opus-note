---
title: 🧁 pacman配置
comments: true
---

## 壹丨pacman配置代理

打开msys终端，执行：

```bash
#export http_proxy='http://username:password@127.0.0.1:3128'
#export ftp_proxy='http://username:password@127.0.0.1:3128'

export http_proxy='http://192.168.6.200:3128'
export https_proxy='http://192.168.6.200:3128'
export ftp_proxy='http://192.168.6.200:3128'
```

参考：[pacman使用代理服务器](https://cloud-atlas.readthedocs.io/zh-cn/latest/linux/arch_linux/pacman_proxy.html)

## 贰丨pacman配置源

第一步，打开配置文件：MSYS2终端上，打开以下文件

```bash
nano /etc/pacman.d/mirrorlist.mingw32
nano /etc/pacman.d/mirrorlist.mingw64
nano /etc/pacman.d/mirrorlist.msys
```

第二步，每个文件顶部添加国内镜像源，如中科大源：

```toml
Server = https://mirrors.ustc.edu.cn/msys2/$repo/$arch
```

第三步，更新数据：

```bash
pacman -Syyu
```

## 叁丨pcaman禁用SSL验证

第一步，打开配置文件

```bash
nano /etc/pacman.conf
```

第二步，修改配置，在`[options]`部分

```toml
[options]
SigLevel = Never
```

第三步，更新数据：

```
pacman -Syu
```

> 恢复SSL验证：
>
> ```toml
> [options]
> SigLevel = Required
> ```
> 



## 肆丨pacman卸载包

搜索相关名称的包：

```bash
pacman -Q | grep mingw-w64
```

卸载`mingw-w64-ucrt-x86_64`前缀的包

```bash
pacman -Rns $(pacman -Qq | grep mingw-w64-ucrt-x86_64)
```



