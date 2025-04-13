---
title: 常用宏定义和宏替换指令
date: 2025.04.12
---

| 宏指令           | 作用                                    | 语法                                        | 示例                                                 |
|---------------|---------------------------------------|-------------------------------------------|----------------------------------------------------|
| `#define`     | 定义简单的宏替换，用于常量定义或简单的代码替换。              | `#define 标识符 替换文本`                        | `#define PI 3.14159`                               |
| `#undef`      | 取消已定义的宏。                              | `#undef 标识符`                              | `#undef PI`                                        |
| `#ifdef`      | 条件编译，如果标识符已被定义，则编译后续代码。               | `#ifdef 标识符`                              | `#ifdef DEBUG`                                     |
| `#ifndef`     | 条件编译，如果标识符未被定义，则编译后续代码。               | `#ifndef 标识符`                             | `#ifndef DEBUG`                                    |
| `#else`       | 条件编译，与`#ifdef`或`#ifndef`配合使用，表示否则的情况。 | `#else`                                   | `#ifdef DEBUG ... #else ...`                       |
| `#endif`      | 结束条件编译块。                              | `#endif`                                  | `#ifdef DEBUG ... #endif`                          |
| `#if`         | 条件编译，根据表达式的值决定是否编译后续代码。               | `#if 常量表达式`                               | `#if VERSION > 2`                                  |
| `#elif`       | 条件编译，与`#if`配合使用，表示否则如果的情况。            | `#elif 常量表达式`                             | `#if VERSION > 2 ... #elif VERSION == 2 ...`       |
| `##`          | 用于宏定义中的连接操作，将两个标记连接成一个标记。             | `#define PASTE(a, b) a##b`                | `PASTE(name, num)` 生成 `namenum`                    |
| `#`           | 用于宏定义中的字符串化操作，将宏参数转换为字符串。             | `#define STR(x) #x`                       | `STR(test)` 生成 `"test"`                            |
| `VA_ARGS`     | 用于定义可变参数的宏。                           | `#define MACRO(...) do { ... } while (0)` | `#define LOG(fmt, ...) printf(fmt, ##__VA_ARGS__)` |
| `__FILE__`    | 预定义宏，表示当前文件的名称。                       | `__FILE__`                                | `printf("File: %s\n", __FILE__);`                  |
| `__LINE__`    | 预定义宏，表示当前行号。                          | `__LINE__`                                | `printf("Line: %d\n", __LINE__);`                  |
| `__DATE__`    | 预定义宏，表示编译日期。                          | `__DATE__`                                | `printf("Date: %s\n", __DATE__);`                  |
| `__TIME__`    | 预定义宏，表示编译时间。                          | `__TIME__`                                | `printf("Time: %s\n", __TIME__);`                  |
| `__func__`    | 预定义宏，表示当前函数的名称。                       | `__func__`                                | `printf("Function: %s\n", __func__);`              |
| `__cplusplus` | 预定义宏，表示C++编译器。                        | `__cplusplus`                             | `#ifdef __cplusplus ... #endif`                    |
| `NDEBUG`      | 预定义宏，用于控制断言的启用。                       | `#define NDEBUG`                          | `#ifdef NDEBUG ... #endif`                         |

