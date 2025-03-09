---
title: Rust踩坑记录
date: 2024.07.01
---

### 1. 报错`error: linking with `C:\mingw64\bin\gcc.exe` failed: exit code: 1`

【问题分析】

mingw64不兼容导致，需要替换为UCRT runtime的版本[^1]

【解决方法】

从winlibs.com[^2]下载MinGW64，然后替换原有文件

【@2025.02，新解决方法】

切换工具链

```bash
# 第一步，安装工具链（可跳过）
rustup toolchain install stable-x86_64-pc-windows-gnu
# 第二步，切换工具链
rustup default stable-x86_64-pc-windows-gnu
```

### 2. RustRover获取`Rust stdlib`需要很长时间

执行：`rustup component add rust-src`

### 3. Rust查找库







[^1]: GitHub Issues，[error: linking with x86_64-w64-mingw32-gcc failed: exit code: 1 #91146](https://github.com/rust-lang/rust/issues/91146#issuecomment-1556081181)
[^2]: winlibs.com，[WinLibs standalone build of GCC and MinGW-w64 for Windows](https://winlibs.com/)
