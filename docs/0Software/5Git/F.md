---
title: Git技巧
comments: true
date: 2024.10.23
---

### 1. `.gitignore`屏蔽A文件夹下除B以外的文件

假设以下目录结构，需要屏蔽除`koko_learn`外的文件夹

```bash
src
├─1012deal
├─FEM
└─koko_learn
```

在`.gitignore`中：

```bash
src/*
!src/koko_learn/
```

!!! warning 

	如果使用了`!src/koko_learn/**`，则会导致`src/koko_learn/base.py`等文件保持在被屏蔽的状态
	
	```bash
	(koko-learn) PS D:\Projects\PycharmProjects\koko-learn> git add .\src\koko_learn\base.py
	hint: Use -f if you really want to add them.
	hint: Disable this message with "git config advice.addIgnoredFile false"
	```

### 2. 删除远程分支上的文件

当设置`.gitignore`前就提交了某文件，在配置后不会自动删除远程分支上的文件

以`src/koko_learn/base.py`和`src/koko_learn/__pycache__`为例：

```bash
# git库将删除文件，本地文件将保留
git rm -r --cached .\src\koko_learn\__pycache__\
git rm --cached .\src\koko_learn\base.py

# 提交修改
git commit -m ":heavy_minus_sign: 删除.gitignore缓存"

# 推送
git push
```

### 3. 强制覆盖远程分支

1. 重置本地分支到远程分支

```bash
git fetch origin
git reset --hard origin/<branch_name>
```

2. 强制推送本地分支到远程分支

```bash
git push --force origin <branch_name>
```

### 4. 强制回滚到某次提交

!!! note "将本地分支重置到指定提交"

    ```bash
    # 硬重置，将丢弃工作目录中所有修改
    git reset --hard <commit_hash>
    
    # 软重置，将保留工作目录中的更改
    git reset --soft <commit_hash>
    
    # 混合重置，默认，保留工作目录修改，放弃暂存区的修改
    git reset <commit_hash>
    ```

强制推送到远程仓库

```bash
git push --force origin <branch_name>
```
