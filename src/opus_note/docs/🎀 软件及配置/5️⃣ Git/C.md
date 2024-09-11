---
title: 🥏 Git Commit规范
comments: true
---

Git 提交信息的标准格式有助于提高代码库的可读性和可维护性。一个常见的标准格式是 **Conventional Commits** 规范，它定义了一种结构化的提交信息格式，使得提交历史更清晰、更有意义。

## 壹丨Conventional Commits 格式

```bash
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

#### 1. `<type>`：提交类型

`<type>` 用于描述提交的类别，常见的类型包括：

- `feat`：新功能
- `fix`：修复问题
- `docs`：仅文档更改
- `style`：格式（不影响代码运行的变动）
- `refactor`：重构（即不是新增功能，也不是修改 bug 的代码变动）
- `test`：添加测试
- `chore`：构建过程或辅助工具的变动

#### 2. `<scope>`：提交范围（可选）

`<scope>` 用于描述提交影响的范围，例如模块、文件或功能。它是可选的，但有助于理解提交的影响范围。

#### 3. `<subject>`：提交说明

`<subject>` 是对提交的简短描述，通常不超过 50 个字符。它应该简洁明了，描述提交的主要变更。

#### 4. `<body>`：详细描述（可选）

`<body>` 是对提交的详细描述，可以包含多行内容。它用于解释为什么进行这些变更，以及变更的具体内容。

#### 5. `<footer>`：脚注（可选）

`<footer>` 通常用于引用相关的任务或问题跟踪系统中的条目，例如 JIRA 票据或 GitHub Issues。它也可以用于描述破坏性变更（BREAKING CHANGE）。

## 贰丨示例

#### 示例 1：新增功能

```
feat(auth): add login functionality

Implemented the login functionality using JWT tokens. Users can now log in with their email and password.
```

#### 示例 2：修复问题

```
fix(api): correct user data endpoint

Fixed the issue where the user data endpoint was returning incorrect data. The endpoint now correctly returns user information.
```

#### 示例 3：文档更改

```
docs(readme): update installation instructions

Updated the installation instructions to include steps for setting up the development environment.
```

#### 示例 4：代码格式

```
style(css): format CSS files

Formatted the CSS files to follow the project's style guidelines. No functional changes.
```

#### 示例 5：重构代码

```
refactor(user): refactor user service

Refactored the user service to improve code readability and maintainability. No functional changes.
```

#### 示例 6：添加测试

```
test(auth): add tests for login functionality

Added unit tests for the login functionality to ensure it works as expected.
```

#### 示例 7：构建过程变动

```
chore(deps): update dependencies

Updated project dependencies to their latest versions.
```

#### 示例 8：破坏性变更

```
feat(api): change user data endpoint

BREAKING CHANGE: The user data endpoint has been changed to /api/v2/user. Update your API calls accordingly.
```

