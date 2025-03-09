---
title: 常用命令(rustc)
date: 2025.02.08
comments: true
---



| 命令                                     | **功能描述**                                                 |
| ---------------------------------------- | ------------------------------------------------------------ |
| `rustc --version`                        | 显示 `rustc` 的版本信息，包括编译器版本、主机目标平台等      |
| `rustc --help`                           | 显示 `rustc` 的帮助信息，包括所有可用的选项                  |
| `rustc <file.rs>`                        | 编译指定的 Rust 源文件，生成可执行文件（默认名称为 `file`）  |
| `rustc -o <output> <file.rs>`            | 编译指定的 Rust 源文件，并将输出的可执行文件命名为 `<output>` |
| `rustc --crate-type lib <file.rs>`       | 编译源文件为库（默认生成 `.rlib` 文件）                      |
| `rustc --crate-type bin <file.rs>`       | 编译源文件为可执行文件（默认行为）                           |
| `rustc --crate-name <name> <file.rs>`    | 指定生成的 crate 名称（默认为文件名）                        |
| `rustc -C opt-level=<level>`             | 设置优化级别（`0`：无优化，`1`：基础优化，`2`：更多优化，`3`：最大优化） |
| `rustc -C debuginfo=<level>`             | 设置调试信息级别（`0`：无调试信息，`1`：行号，`2`：完整调试信息） |
| `rustc -C target-cpu=<cpu>`              | 指定目标 CPU 架构，以优化生成的代码                          |
| `rustc -C target-feature=<features>`     | 启用特定的 CPU 特性（如 `+sse2`、`+avx` 等）                 |
| `rustc -C lto`                           | 启用链接时优化（Link-Time Optimization, LTO）                |
| `rustc -C codegen-units=<units>`         | 设置代码生成单元的数量，减少编译时间（默认为 `1`，值越大编译速度越快，但优化效果越差） |
| `rustc -Z print-link-args`               | 打印链接器参数，用于调试链接问题                             |
| `rustc --emit=llvm-ir <file.rs>`         | 生成 LLVM IR 文件，用于调试或分析                            |
| `rustc --emit=asm <file.rs>`             | 生成汇编代码文件，用于调试或分析                             |
| `rustc --emit=mir <file.rs>`             | 生成中间表示（MIR）文件，用于调试或分析                      |
| `rustc --emit=dep-info <file.rs>`        | 生成依赖信息文件，用于构建系统                               |
| `rustc --target <triple>`                | 指定目标平台（如 `x86_64-unknown-linux-gnu`、`armv7-linux-androideabi` 等） |
| `rustc -L <path>`                        | 添加库路径，用于链接外部库                                   |
| `rustc -l <lib>`                         | 链接指定的外部库                                             |
| `rustc -g`                               | 启用调试信息（等同于 `-C debuginfo=2`）                      |
| `rustc -O`                               | 启用优化（等同于 `-C opt-level=3`）                          |
| `rustc --edition=<edition>`              | 指定 Rust 版本（如 `2015`、`2018`、`2021` 等）               |
| `rustc --explain <error>`                | 解释指定的错误代码，提供详细的错误信息和解决方案             |
| `rustc --crate-type=cdylib <file.rs>`    | 编译源文件为动态链接库（CDYLIB）                             |
| `rustc --crate-type=staticlib <file.rs>` | 编译源文件为静态库（C 风格的静态库）                         |
| `rustc --test <file.rs>`                 | 编译并运行测试代码                                           |
| `rustc --bench <file.rs>`                | 编译并运行基准测试代码                                       |
| `rustc --example <example>`              | 编译并运行指定的示例代码                                     |

