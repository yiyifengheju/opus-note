---
title: pub mode
date: 2025.02.08
comments: true
---

__`pub mod`__: 定义的模块在整个 crate 外部可见，其他 crate 可以访问。

__`pub(crate) mod`__: 定义的模块仅在当前 crate 内部可见，其他 crate 不能访问。

### 1. `pub mod`

- __可见性__: 使用 `pub mod` 定义的模块在整个 crate（包）外部都是可见的。这意味着其他 crate 可以使用这个模块中的内容。
- __使用场景__: 当你想要让其他 crate 访问这个模块时，使用 `pub mod`。

```rust
// src/lib.rs
pub mod my_module {
    pub fn my_function() {
        println!("Hello from my_function!");
    }
}

// src/main.rs (或者其他 crate)
use my_crate::my_module;

fn main() {
    my_module::my_function(); // 可以访问
}
```

### 2. `pub(crate) mod`

- __可见性__: 使用 `pub(crate) mod` 定义的模块仅在当前 crate 内部可见。这意味着其他 crate 不能访问这个模块。
- __使用场景__: 当你希望模块只能被当前 crate 内部的代码使用时，使用 `pub(crate) mod`。

```rust
// src/lib.rs
pub(crate) mod my_internal_module {
    pub fn my_internal_function() {
        println!("Hello from my_internal_function!");
    }
}

// src/main.rs (或者其他 crate)
fn main() {
    // my_internal_module::my_internal_function(); // 不能访问，编译错误
}
```

