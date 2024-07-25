---
title: B 跳过Fancybox渲染
comments: true
---

### 1. 思路

1. 不通过Fancybox展示的图片添加跳过的类名，如`no-fancybox`
2. 修改`fancybox.js`，遇到上述类名直接跳过

### 2. 方案

修改`themes/next/source/js/third-party/fancybox.js`：

```js
document.querySelectorAll('.post-body :not(a) > img, .post-body > img').forEach(image => {
+    if ($image.is('.no-fancybox img')) {
+      return;
+    }
```

然后，为图片添加：

```html
<img class="no-fancybox" src="" alt="">
```