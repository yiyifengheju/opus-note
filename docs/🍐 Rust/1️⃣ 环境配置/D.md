---
title: 常用命令(rustup)
date: 2024.02.15
comments: true
---



| **命令**                              | **功能描述**                                                 | **示例**                                        |
| ------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------- |
| `rustup install <toolchain>`          | 安装指定的工具链                                             | `rustup install stable-x86_64-pc-windows-gnu`   |
| `rustup default <toolchain>`          | 设置默认的工具链                                             | `rustup default stable-x86_64-pc-windows-gnu`   |
| `rustup update`                       | 更新所有已安装的工具链                                       | `rustup update`                                 |
| `rustup update <toolchain>`           | 更新指定的工具链                                             | `rustup update stable`                          |
| `rustup toolchain list`               | 列出所有已安装的工具链                                       | `rustup toolchain list`                         |
| `rustup toolchain remove <toolchain>` | 卸载指定的工具链                                             | `rustup toolchain remove nightly`               |
| `rustup override set <toolchain>`     | 在当前目录设置工具链覆盖                                     | `rustup override set stable`                    |
| `rustup override unset`               | 取消当前目录的工具链覆盖                                     | `rustup override unset`                         |
| `rustup component add <component>`    | 安装指定组件（如编译器工具、标准库等）                       | `rustup component add rust-src`                 |
| `rustup component remove <component>` | 卸载指定组件                                                 | `rustup component remove rust-src`              |
| `rustup component list`               | 列出当前工具链可用的组件                                     | `rustup component list`                         |
| `rustup target add <target>`          | 添加目标三元组以支持交叉编译                                 | `rustup target add x86_64-unknown-linux-gnu`    |
| `rustup target remove <target>`       | 移除目标三元组                                               | `rustup target remove x86_64-unknown-linux-gnu` |
| `rustup target list`                  | 列出所有支持的目标三元组                                     | `rustup target list`                            |
| `rustup run <toolchain> <command>`    | 在指定工具链下运行命令                                       | `rustup run stable cargo build`                 |
| `rustup which <command>`              | 显示指定命令的实际路径                                       | `rustup which rustc`                            |
| `rustup show`                         | 显示当前安装的工具链和默认工具链信息                         | `rustup show`                                   |
| `rustup set profile <profile>`        | 设置 `rustup` 的配置文件（如 `default`, `minimal`, `complete`） | `rustup set profile complete`                   |
| `rustup self update`                  | 更新 `rustup` 自身                                           | `rustup self update`                            |
| `rustup self uninstall`               | 卸载 `rustup`                                                | `rustup self uninstall`                         |

