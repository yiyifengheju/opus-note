---
title: 🍘 使用`Literal`提高Python代码的类型安全性
date: 2024.07.24
comments: true
---

在现代软件开发中，类型安全性和代码可读性是两个非常重要的方面。为了提高类型安全性，Python引入了`typing`模块。

## 壹丨什么是`Literal`

`Literal`是Python3.8引入的一个类型注解，用于指定一个变量或参数只能是某些特定的值。通过使用`Literal`，可以在代码中明确地表达某些变量只能取特定的值，从而提高代码的类型安全性和可读性。以下是[Python官方文档](https://docs.python.org/zh-cn/3/library/typing.html#typing.Literal)的注解：

>**typing.Literal**
>
>特殊类型注解形式，用于定义“字面值类型”。
>
>`Literal`可以用来向类型检查器说明被注解的对象具有与所提供的字面量之一相同的值。
>
>例如：
>
>```python
>def validate_simple(data: Any) -> Literal[True]:  # always returns True
>    ...
>
>type Mode = Literal['r', 'rb', 'w', 'wb']
>def open_helper(file: str, mode: Mode) -> str:
>    ...
>
>open_helper('/some/path', 'r')      # Passes type check
>open_helper('/other/path', 'typo')  # Error in type checker
>```
>
>`Literal[...]`不能创建子类。在运行时，任意值均可作为`Literal[...]`的类型参数，但类型检查器可以对此加以限制。字面量类型详见[**PEP586**](https://peps.python.org/pep-0586/)。
>
>> *Addedinversion3.8.*
>
>> *在3.9.1版本发生变更:*`Literal`现在能去除形参的重复。`Literal`对象的相等性比较不再依赖顺序。现在如果有某个参数不为[hashable](https://docs.python.org/zh-cn/3/glossary.html#term-hashable)，`Literal`对象在相等性比较期间将引发[`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError)。

## 贰丨基本用法

```python
from typing import Literal


def my_method(param: Literal['option1', 'option2']
              ) -> None:
    if param == 'option1':
        print("Option1 selected")
    elif param == 'option2':
        print("Option2 selected")


# 正确的用法
my_method('option1')  # 输出:Option1 selected
my_method('option2')  # 输出:Option2 selected

# 错误的用法，类型检查工具会报错
my_method('option3')  # 类型检查工具会报错，因为 'option3' 不在 Literal['option1', 'option2'] 中
```

在这个例子中，`process_status`函数的参数`status`被注解为`Literal['open','closed','pending']`，这意味着`status`只能是`'open'`、`'closed'`或`'pending'`。如果传递其他值，类型检查工具（如`mypy`、`pytype`、`Pylint`等）会报错。

## 叁丨在抽象方法中使用`Literal`

在面向对象编程中，经常使用抽象基类和抽象方法来定义接口。`Literal`也可以与`@abstractmethod`装饰器结合使用，以确保子类实现的方法参数符合特定的值。

```python
from abc import ABC, abstractmethod
from typing import Literal


class MyBaseClass(ABC):
    @abstractmethod
    def my_method(self, 
                  param: str) -> None:
        pass


class MyConcreteClass(MyBaseClass):
    def my_method(self, 
                  param: Literal['option1', 'option2']) -> None:
        if param == 'option1':
            print("Option1 selected")
        elif param == 'option2':
            print("Option2 selected")


# 示例用法
obj = MyConcreteClass()
obj.my_method('option1')  # 输出:Option1 selected
obj.my_method('option2')  # 输出:Option2 selected
```

在这个例子中，父类`MyBaseClass`中的抽象方法`my_method`的参数类型是`str`，表示可以接受任何字符串。子类`MyConcreteClass`中实现了`my_method`，并将参数类型具体化为`Literal['option1', 'option2']`，表示只能接受`'option1'`或`'option2'`。

> 在这里，父类限定了`['option1', 'option2']`后，子类中必须使用同样的`['option1', 'option2']`

### TIP丨在抽象方法中使用`Literal`进行类型收窄

在某些情况下，实现子类时会遇到不同子类间可接受的注解取值范围不同。这时可以对父类方法的参数类型放宽约束为`str`，进而在子类上使用`Literal`进行更严格的约束。

```python
from abc import ABC, abstractmethod
from typing import Literal


class MyBaseClass(ABC):
    @abstractmethod
    def my_method(self, 
                  param: str) -> None:
        pass


class MyConcreteClass(MyBaseClass):
    def my_method(self,
                  param: Literal['option1', 'option2']) -> None:
        if param == 'option1':
            print("Option1 selected")
        elif param == 'option2':
            print("Option2 selected")


# 示例用法
obj = MyConcreteClass()
obj.my_method('option1')  # 输出:Option1 selected
obj.my_method('option2')  # 输出:Option2 selected
```

在这个例子中，子类`MyConcreteClass`对父类`MyBaseClass`的抽象方法`my_method`的参数类型进行了收窄，从`str`收窄为`Literal['option1','option2']`。这种做法是允许的，因为`Literal['option1','option2']`是`str`的子类型，符合类型约束的收窄原则。