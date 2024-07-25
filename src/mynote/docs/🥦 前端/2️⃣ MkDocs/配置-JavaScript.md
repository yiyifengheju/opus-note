---
title: 配置-JavaScript
comments: true
---

## 壹丨JavaScript文件

### 1. mathjax.js

用于渲染公式

=== ":material-file: docs/javascripts/mathjax.js"

    ```JavaScript
    window.MathJax = {
        tex: {
            inlineMath: [["\\(", "\\)"]], displayMath: [["\\[", "\\]"]], processEscapes: true, processEnvironments: true
        }, options: {
            ignoreHtmlClass: ".*|", processHtmlClass: "arithmatex"
        }
    };
    document$.subscribe(() => {
        MathJax.typesetPromise()
    })
    ```

=== ":material-file: mkdocs.yml"

    ``` yaml
    extra_javascript:
      - javascripts/mathjax.js
      - https://polyfill.io/v3/polyfill.min.js?features=es6
      - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
    ```

## 贰丨其他

!!! tip

	lazyload.iife.js、load_img.js及用法见[xx]()
	
	travel_card.js及用法见[xx]()
	
	bbly.js及用法见[xx]()



??? tip "2-3具体用法见[xxx]()"
    
    用于图片的懒加载，见[`vanilla-lazyload`](https://www.npmjs.com/package/vanilla-lazyload?activeTab=readme)

