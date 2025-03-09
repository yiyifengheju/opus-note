---
title: 🧁 mingw64版本区别
comments: true
---



| __属性__         | __mingw64__      | __ucrt64__       | __clang64__               | __clangarm64__           |
|-------------------|------------------|------------------|---------------------------|--------------------------|
| __编译器__        | GCC              | GCC              | Clang/LLVM               | Clang/LLVM              |
| __目标架构__      | x86_64 (64位)    | x86_64 (64位)    | x86_64 (64位)            | ARM64                   |
| __运行时库__      | msvcrt           | ucrt             | ucrt                     | ucrt                    |
| __C库__           | MSVCRT           | UCRT             | UCRT                     | UCRT                    |
| __C++标准库__     | libstdc++        | libstdc++        | libc++/libstdc++         | libc++/libstdc++        |
| __适用场景__      | 传统64位程序开发 | 现代Windows开发（Win10+）、兼容性更好 | LLVM生态集成、跨平台开发 | ARM设备Windows开发（如Surface Pro X） |
| __ABI兼容性__     | 旧版Windows      | 现代Windows（MSVC） | 现代Windows（MSVC）      | 现代Windows（MSVC）     |
| __支持的C标准__   | C89/C99（部分支持） | C11/C17（完整支持） | C11/C17/C23（部分支持）  | C11/C17/C23（部分支持） |

### 关键区别说明

#### 1. 运行时库

* __msvcrt__：旧版Microsoft C运行时库（WinXP~Win7兼容，但功能受限）。

* __ucrt__：通用C运行时库（Win10+默认），支持完整C11/C17标准，兼容现代MSVC程序。

#### 2. 编译器

* __GCC__：传统MinGW工具链，依赖GNU生态。
* __Clang__：支持更现代的C/C++标准（如C++20/23），更好的MSVC兼容性。

#### 3. 目标架构

* __x86_64__：主流64位Windows程序。
* __ARM64__：专为ARM架构Windows设备优化（如高通芯片设备）。

#### 4. C++标准库

* __libstdc++__：GCC配套库，兼容性好但更新较慢。
* __libc++__：Clang默认库，支持最新C++标准，但需注意兼容性。

#### 5. 适用场景

* 需要兼容旧版Windows（Win7或更早）：`mingw32`/`mingw64`。
* 现代Windows开发（Win10+）或与MSVC交互：`ucrt64`。
* 使用Clang特性或跨平台代码：`clang64`/`clangarm64`。