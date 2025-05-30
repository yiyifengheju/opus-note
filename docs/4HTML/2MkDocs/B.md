---
title: 😆 MkDocs语法备忘
comments: true
---

### 1. 链接在新标签页打开

```markdown
[:fontawesome-solid-paper-plane:](http://baidu.com){:target="_blank" .md-button}
```

[:fontawesome-solid-paper-plane:](http://baidu.com){:target="_blank" .md-button}

### 2. Markdown插入表情
```markdown
:bootstrap-envelope-paper:
```
:bootstrap-envelope-paper:

### 3. 缩写语法词汇表

词汇表：
```markdown title="./lib/abbreviations.md"
*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium
```

The HTML specification is maintained by the W3C.

### 4. 标注语法

可用包括：note、abstract、info、tip、success、question、warning、failure、danger、bug、example、quote

```markdown
!!! note "Phasellus posuere in sem ut cursus"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```
!!! note "Phasellus posuere in sem ut cursus"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

```markdown
??? note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

???+ note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

??? note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

内联块：


!!! info inline end

    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nulla et euismod nulla.
    Curabitur feugiat, tortor non consequat
    finibus, justo purus auctor massa, nec
    semper lorem quam in massa.

```markdown
!!! info inline end

    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nulla et euismod nulla.
    Curabitur feugiat, tortor non consequat
    finibus, justo purus auctor massa, nec

    semper lorem quam in massa.

```

!!! info inline

    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nulla et euismod nulla.
    Curabitur feugiat, tortor non consequat
    finibus, justo purus auctor massa, nec
    semper lorem quam in massa.

```markdown
!!! info inline

    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nulla et euismod nulla.
    Curabitur feugiat, tortor non consequat
    finibus, justo purus auctor massa, nec

    semper lorem quam in massa.
```

### 5. 按钮
```markdown
[按钮](#){ .md-button }
```
[按钮](#){ .md-button }

```markdown
[按钮](#){ .md-button .md-button--primary }
```
[按钮](#){ .md-button .md-button--primary }

```markdown
[按钮 :fontawesome-solid-paper-plane:](#){ .md-button }
```
[按钮 :fontawesome-solid-paper-plane:](#){ .md-button }

### 6. 代码标题
```markdown
'''python title="./script.py"
import numpy as np

array = np.array([1,2,3,4])
'''
```

```python title="./script.py"
import numpy as np

array = np.array([1,2,3,4])
```

### 7. 代码块分组

```markdown
=== "C"
	
    ``` c
    #include <stdio.h>
	
    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
```

=== "C++"

    ``` c++
    #include <iostream>
    
    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```
```

=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
```

=== "C++"

    ``` c++
    #include <iostream>
    
    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```

### 8. 脚注
```markdown
Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]
```
Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]

```markdown
[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
[^2]:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```
[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
[^2]:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

### 9. 带颜色的图标

```markdown
@keyframes heart {
  0%, 40%, 80%, 100% {
    transform: scale(1);
  }
  20%, 60% {
    transform: scale(1.15);
  }
}
.heart {
  animation: heart 1000ms infinite;
  color: #FF0000;
}
</style>

:octicons-heart-fill-24:{ .heart }
```

<style>
@keyframes heart {
  0%, 40%, 80%, 100% {
    transform: scale(1);
  }
  20%, 60% {
    transform: scale(1.15);
  }
}
.heart {
  animation: heart 1000ms infinite;
  color: #FF0000;
}
</style>

:octicons-heart-fill-24:{ .heart }

### 10. 图像设置
```markdown
![Image title](https://dummyimage.com/600x400/eee/aaa){ xxx }
```

左对齐、右对齐
```markdown
{ align=left }
{ align=right }
```

延迟加载
```markdown
{ loading=lazy }
```

### 10. 任务列表

```markdown
- [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
- [ ] Vestibulum convallis sit amet nisi a tincidunt
    * [x] In hac habitasse platea dictumst
    * [x] In scelerisque nibh non dolor mollis congue sed et metus
    * [ ] Praesent sed risus massa
- [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque
```

- [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
- [ ] Vestibulum convallis sit amet nisi a tincidunt
    * [x] In hac habitasse platea dictumst
    * [x] In scelerisque nibh non dolor mollis congue sed et metus
    * [ ] Praesent sed risus massa
- [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque
