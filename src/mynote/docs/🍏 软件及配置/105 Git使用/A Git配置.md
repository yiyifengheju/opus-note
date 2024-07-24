### 1. 查看 Git 版本

使用以下命令可以查看 Git 的版本信息：

```bash
git --version
```

### 2. 配置用户名和邮箱

使用以下命令可以配置 Git 的用户名和邮箱：

```bash
git config --global user.name "yourname"
git config --global user.email "youremail"
```

其中，`yourname`和`youremail`需要替换为自己的用户名和邮箱

### 3. 生成秘钥

使用以下命令可以生成 SSH 秘钥：

```bash
ssh-keygen -t rsa -C "youremail"
```

同样，`youremail`需要替换为自己的邮箱

### 4. 添加秘钥到 GitHub

读取秘钥，并将秘钥添加到GitHub：

```bash
cat ~/.ssh/id_rsa.pub
```

将 id_rsa.pub 文件的内容复制，并将其粘贴到 GitHub 的——Setting——SSH keys——New SSH key中

### 5. 测试连接

使用以下命令测试连接：

```bash
ssh -T git@github.com
```

如果连接成功，会出现提示信息：

```bash
Hi {username}! You've successfully authenticated, but GitHub does not provide shell access.
```

如果连接失败，可以尝试排查和处理连接错误，例如检查网络连接、确认 SSH 秘钥是否正确、检查 GitHub 设置是否正确等等。