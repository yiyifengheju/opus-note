---
title: Argparse
comments: true
---

`argparse` 是 Python 中一个内置库，用于解析命令行参数。它提供了一个简单的方式来处理命令行参数，可以帮助开发者快速创建命令行工具。

文档：https://docs.python.org/3/library/argparse.html


## 壹丨简单使用[^1]

1. 创建一个 `ArgumentParser` 对象
```
# 导入包
import argparse

# 实例化
parser = argparse.ArgumentParser(description='CMD option')
```
2. 定义命令行参数
```
parser.add_argument('--input', '-i', required=True, help='input')
parser.add_argument('--output', '-o', required=True, help='output')
```
在上面的代码中，使用 `add_argument` 方法添加了两个命令行参数：`--input` 和 `--output`。`--input` 是一个可选参数，其中 `-i` 是一个缩写，用于在命令行中使用。`--output` 也是一个可选参数，其中 `-o` 是一个缩写。这两个参数都是必填的，因为在 `add_argument` 方法中将 `required` 参数设置为 `True`。

3. 处理命令行参数
```
args = parser.parse_args()
```
在上面的代码中，使用 `parse_args` 方法处理命令行参数。这个方法返回一个 `Namespace` 对象，其中包含所有命令行参数的值。

4. 使用命令行参数
```
input = args.input
output = args.output
```
在上面的代码中，我们使用 `input` 和 `output` 变量来访问命令行参数的值。

5. 显示帮助信息
```
parser.print_help()
```
在上面的代码中，我们使用 `print_help` 方法显示帮助信息。这个方法将显示所有命令行参数的帮助信息。

6. 处理错误
```
try:
    args = parser.parse_args()
except ArgumentError as e:
    print(e)
```
在上面的代码中，使用 `try`/`except` 块来处理错误。如果命令行参数无法解析，则会引发一个 `ArgumentError` 异常。



## 贰丨实例

```python
import argparse

def main():
    param = argparse.ArgumentParser(description='argparse包演示')
    param.add_argument('-n', '--name', default='MasterMao', type=str, help='姓名')
    param.add_argument('-a', '--age', default=4, type=int)
    args = param.parse_args()
    print(args)

    name = args.name
    print(f'Hello {name} {args.age}')

if __name__ == '__main__':
    main()
```



## 叁丨配合`os.system()`实现自动化脚本

```python
import os

if __name__ == "__main__":
    NAME = ['xiaoming', 'xiaohong', 'xiaoma']
    for name in NAME:
        os.system(f'python utils.py --name {name}')
```




[^1]: CSDN，@骑着蜗牛向前跑，[argparse基本用法](https://blog.csdn.net/yy_diego/article/details/82851661)
