---
title: cargo常用命令
date: 2025.02.08
comments: true
---

| 命令                       | 功能描述                                     |
|--------------------------|------------------------------------------|
| `cargo new <NAME>`       | 创建一个新的 Rust 项目                           |
| `cargo build`            | 编译当前目录下的 Rust 项目（默认为调试模式）                |
| `cargo build --release`  | 以优化模式编译项目，用于生产环境                         |
| `cargo run`              | 编译并运行当前目录下的 Rust 项目                      |
| `cargo run --release`    | 以优化模式编译并运行项目                             |
| `cargo test`             | 运行当前目录下 Rust 项目的所有测试                     |
| `cargo check`            | 检查代码是否可以编译，但不生成可执行文件（比 `cargo build` 更快） |
| `cargo clean`            | 清理项目，删除 `target` 目录及其内容                  |
| `cargo doc`              | 为当前目录下的 Rust 项目生成文档                      |
| `cargo update`           | 更新当前目录下 Rust 项目的依赖                       |
| `cargo install <NAME>`   | 安装指定的 crate 到系统                          |
| `cargo publish`          | 发布 crate 到 crates.io                     |
| `cargo search <TERM>`    | 在 crates.io 上搜索 crate                    |
| `cargo bench`            | 运行项目的基准测试                                |
| `cargo login <TOKEN>`    | 登录到 crates.io                            |
| `cargo owner`            | 管理 crate 的所有者                            |
| `cargo package`          | 打包一个 crate 以发布                           |
| `cargo uninstall <NAME>` | 从系统中卸载一个 crate                           |
| `cargo fmt`              | 使用 `rustfmt` 格式化代码，保持官方风格一致性             |
| `cargo fix`              | 自动修复代码中的常见问题（如编译警告）                      |
| `cargo clippy`           | 使用 `clippy` 检查代码潜在问题和改进建议                |
| `cargo tree`             | 显示项目依赖的层次结构                              |
| `cargo help`             | 查看命令帮助                                   |
| `cargo help <命令>`        | 查看指定命令的帮助信息                              |
| `cargo version`          | 显示 Cargo 的版本信息                           |

