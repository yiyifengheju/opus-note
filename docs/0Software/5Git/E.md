---
title: 🛢️ Git常见错误
comments: true
---

### 1. 网络错误

【问题复现】

```bash
# 代理ON：
fatal: unable to access 'https://github.com/yiyifengheju/ONAV.git/': Error in the HTTP2 framing layer
# 代理OFF：
fatal: unable to access 'https://github.com/yiyifengheju/ONAV.git/': GnuTLS recv error (-110): The TLS connection was non-properly terminated.
```

【解决方法】

```bash
sudo apt-get update
sudo apt-get install gnutls-bin
git config --global http.sslVerify false
git config --global http.postBuffer 1048576000
```

### 2. RPC错误

【问题复现】

```bash
error: RPC failed; curl 16 Error in the HTTP2 framing layer
send-pack: unexpected disconnect while reading sideband packet
fatal: the remote end hung up unexpectedly
```

【解决方法】强制将git设置为HTTP 1.1：

```bash
git config --global http.version HTTP/1.1
```

> 恢复方法：
>
> ```bash
> git config --global http.version HTTP/2
> ```

### 3. WSL代理问题

【问题复现】打开WSL时显示：

```bash
wsl: 检测到 localhost 代理配置，但未镜像到 WSL。NAT 模式下的 WSL 不支持 localhost 代理。
```

【解决方法】在Windows中的`C:\Users\$Username$\`目录下创建一个`.wslconfig`文件，然后在文件中写入如下内容：

```toml
[experimental]
autoMemoryReclaim=gradual  
networkingMode=mirrored
dnsTunneling=true
firewall=true
autoProxy=true
```

### 4. 每次git都需要输入用户名和密码

【问题复现】如题

【解决方法】执行下述命令后，再执行`git pull`或`git push`，输入用户名密码，以后就不需要每次都输入了。

```bash
git config --global credential.helper store
```

### 5. 报ssh拒绝连接，无法`git clone`

```bash
ssh -T git@github.com
# ssh: connect to host github.com port 22: Connection refused
```

解决方法：新建文件`~/.ssh/config`，写入：

```bash
Host github.com
Hostname ssh.github.com
port 443
```







