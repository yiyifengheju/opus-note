---
title: 🐖 文件操作
comments: true
---

### 1. Python获取图片大小

```python
size = sys.getsizeofimage(img)
```

### 2. 删除文件

问题描述：使用Loguru对每个数据文件生成日志，导致最终磁盘写满。因而写了个`txt2yaml`函数，在数据转换完成后，使用`os.system(f'rm {log_path}')`删除`.txt`日志文件，但在程序运行中发现没有删除

原因分析：缓冲区与磁盘不同步，缓冲区的数据没有被删除

解决方法：强制同步缓冲区和磁盘，再执行删除

```python
with open(log_path, 'w') as f:
    os.fsync(f.fileno())
#os.system(f'rm {log_path}')
os.remove(log_path)
```

!!! note

	更高效的方法是直接使用`os.remove(log_path)`，会先将文件从内存中删除，再进行磁盘同步的操作，一般不会出现缓冲区和磁盘不同步的情况，但当文件不存在或没有删除权限时，会报错

