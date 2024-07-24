---
title: 🏀 getattr()动态获取对象属性和方法
comments: true
---

## 壹丨什么是getattr()函数

`getattr()`是Python内置函数之一，用于获取对象的属性或方法。

```python
getattr(object, attribute_name[, default_value])
```

- `object`是要获取属性或方法的对象。
- `attribute_name`是要获取的属性或方法的名称。
- `default_value`是可选参数，表示在属性或方法不存在时返回的默认值。

## 贰丨使用方法

### 1. 获取对象的属性值

```python
class Person:
    name = "Alice"
    age = 30

person = Person()
name = getattr(person, "name")
print(name)  # Output: "Alice"
```

### 2. 获取对象的方法

```python
class Calculator:
    def add(self, x, y):
        return x + y

calc = Calculator()
method = getattr(calc, "add")
result = method(3, 4)
print(result)  # Output: 7
```

### 3. 处理动态属性名

```python
class Config:
    def __init__(self):
        self.debug_mode = True
        self.verbose_mode = False

config = Config()
mode = "debug_mode"
value = getattr(config, mode)
print(value)  # Output: True
```

## 叁丨为什么要使用getattr()函数？

1. **灵活性**：根据变量的值动态访问对象的属性或方法。
2. **可扩展性**：方便添加新的属性或方法，而不需要修改代码。
3. **简洁性**：避免大量的条件判断语句，使代码更加简洁和易读。
4. **Pythonic风格**：符合Python的动态特性和简洁性。

通过使用`getattr()`函数，可以更好地处理动态数据和对象，使代码更具通用性和灵活性。在实际编程中，合理利用`getattr()`函数可以提高代码的可维护性和可扩展性。
