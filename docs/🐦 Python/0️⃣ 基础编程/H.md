---
title: 🐖 抽象基类
comments: true
---

当类继承ABC时，添加@abstractmethod装饰器的函数和普通函数有什么区别？@abstractmethod的函数是必须要重写的吗？没有@abstractmethod是否一般不需要重写？

> 继承`ABC`的抽象基类无法实例化，@abstractmethod装饰的抽象方法必须重写，没有装饰器的可以选择性重写



!!! warning "以下内容由AI生成"

在 Python 中，`ABC`（Abstract Base Class）模块提供了一个机制来定义抽象基类。抽象基类允许你定义接口或基类，其中包含一个或多个抽象方法。抽象方法是指在基类中定义但没有实现的方法，子类必须实现这些方法。

### `@abstractmethod` 的作用

当你在一个类中使用 `@abstractmethod` 装饰器标记一个方法时，这个方法就成为了一个抽象方法。抽象方法在基类中没有实现，任何继承这个基类的子类都必须实现这些抽象方法，否则无法实例化子类。

### 普通方法与抽象方法的区别

- **抽象方法**：使用 `@abstractmethod` 装饰器标记的方法，必须在子类中实现，否则子类无法实例化。
- **普通方法**：在基类中定义并实现的方法，子类可以选择性地重写这些方法，但不是必须的。

### 示例

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("Sleeping...")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

# 尝试实例化 Animal 会报错
try:
    animal = Animal()
except TypeError as e:
    print(e)  # "Can't instantiate abstract class Animal with abstract methods make_sound"

# 实例化 Dog 并调用方法
dog = Dog()
dog.make_sound()  # 输出 "Bark"
dog.sleep()       # 输出 "Sleeping..."
```



