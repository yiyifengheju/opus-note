---
title: G Pycharm配置
comments: true
---

### 1. 代码模板

>CN：设置 —— 编辑器 —— 文件和代码模板 —— Python Script


```python
"""
=========================================================================
@File Name: ${NAME}.py
@Time: ${DATE} ${TIME}
@Program IDE：${PRODUCT_NAME}
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 
- 
=========================================================================
"""
```

??? note "附：PyCharm关键字"

	```
	${NAME} - 新建文件过程中设置的新文件名称；
	${DATE} - 系统日期；
	${TIME} - 系统时间；
	${PRODUCT_NAME} - 创建文件所用IDE的名称；
	${PROJECT_NAME} - 项目名称；
	${USER} - 当前登录的用户名；
	${YEAR} - 年；
	${MONTH} - 月；
	${DAY} - 日；
	${HOUR} - 时；
	${MINUTE} - 分；
	${MONTH_NAME_SHORT} - 月份缩写；
	${MONTH_NAME_FULL} - 月份全名。
	```

### 2. 函数参数注释格式

>CN：工具 —— Python集成工具 —— Docstring —— numpy


注释格式举例：

```python
import numpy as np

def add(a, b):
    """
    Add two arrays element-wise.

    Parameters
    ----------
    a : ndarray
        The first array.
    b : ndarray
        The second array.

    Returns
    -------
    ndarray
        The sum of the two arrays.
    """
    return np.add(a, b)
```

### 3. 代码自动补全忽略大小写[^1]

JetBrains默认设置的代码自动补全区分大小写。

> EN：Settings —— Editor —— General —— Code Completion —— 取消勾选`Match case`
> 
> CN：设置 —— 编辑器 —— 常规 —— 代码补全 —— 取消勾选“区分大小写”

或

> 直接搜索`Code Completion`或`代码补全`


![image-20230729003610966](https://my-gallery-1306340269.cos.ap-beijing.myqcloud.com/mastermao/image-20230729003610966.png)

### 4. 关闭相似代码提示

> EN：Preferences——Editor——Inspections——General——Duplicated code fragment，取消勾选

### 5. 插件

* Chinese（Simplified）Language Pack/中文语言包 
* WebP Support——支持`.webp`图片
* IKun Progress——个性化进度条
* Ruff——代码格式化工具
* Full Line Code Completion——代码补全工具
* SonarLint——代码检查工具


[^1]: 博客园，@楼兰胡杨，[IntelliJ IDEA 设置代码自动补全不区分大小写](https://www.cnblogs.com/east7/p/15565729.html)
