---
title: F pip升级第三方库
comments: true
---
## 壹丨升级单个库

第一步，升级pip

```bash
python -m pip install --upgrade pip
```

第二步，查看所有可升级库

```bash
pip list --outdated
# 或
pip list -o
```

第三步，升级单个库

```bash
pip install <库名> --upgrade
```

## 贰丨使用脚本实现一键升级

```python
import os

# 升级pip
command = 'python -m pip install --upgrade pip'
os.system(command)

# 获取pip列表
command = 'pip list -o'
cmd_data = os.popen(command)

# 升级包
contents = cmd_data.readlines()[2:]
for line in contents:
    package = line.split(" ")[0]
    if package == "WARNING:":
        continue
    print()
    print(f'检查更新包: {package}')
    os.system(f'pip install {package} --upgrade')
print("更新完毕")
```

