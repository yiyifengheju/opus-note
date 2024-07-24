---
title: F Ubuntu设置Samba
comments: true
---

### 第一步，安装Samba[^1]

```bash
sudo apt update
sudo apt install samba
```

> 检查是否安装成功：
>
> ```bash
> whereis samba
> ```
>
> 输出：
>
> ```bash
> samba: /usr/sbin/samba /usr/lib/x86_64-linux-gnu/samba /etc/samba /usr/share/samba /usr/share/man/man7/samba.7.gz /usr/share/man/man8/samba.8.gz
> ```

### 第二步，设置共享文件夹

这里设置的共享目录为`~/samba`

```bash
mkdir ~/samba
```

### 第三步，修改配置文件

```bash
sudo nano /etc/samba/smb.conf
```

在底部添加：

```ini
[sambashare]
    comment = Samba on Ubuntu
    path = /home/mastermao/samba
    read only = no
    browsable = yes
    public = yes
    available = yes
    guest ok = no
    writable = yes
    valid users = mastermao
    create mask = 0777
    directory mask = 0777
```

### 第四步，更新防火墙规则允许Samba

```bash
sudo ufw allow samba
```

### 第五步，设置用户账户

```bash
sudo smbpasswd -a mastermao
```

设置账户密码后即可保存

### 第六步，重启Samba服务

```bash
sudo service smbd restart
```

### 最后，Windows访问

文件资源管理器地址栏输入：`\\192.168.0.107`，即可打开Samba共享文件夹





[^1]: CSDN，@orange....，https://blog.csdn.net/Cfx1998/article/details/128974277
