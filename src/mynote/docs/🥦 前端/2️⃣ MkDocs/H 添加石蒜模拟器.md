---
title: H 添加石蒜模拟器
date: 2024.03.03
comments: true
---

CSS：

```css
.content-sakana {
  display: flex;
  align-items: flex-end;
  max-height: 80px;
}
.md-typeset h1 {
  color: var(--md-default-fg-color--light);
  font-size: 2em;
  line-height: 1.3;
  margin: 0 0 1.25em;
  margin-right: auto;
  }
#sakana-widget {
  margin: 0 0 1.25em;
  padding-left: 60%;
  overflow: visible;
  }
```

HTML

```html
{% if "\x3ch1" not in page.content %}
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/sakana-widget@2.7.0/lib/sakana.min.css"
    />
    <div class="content-sakana">
  <h1>{{ page.title | d(config.site_name, true)}}</h1>

    <div id="sakana-widget"></div>
    </div>
    <script>
      function initSakanaWidget() {
        new SakanaWidget().mount('#sakana-widget');
      }
    </script>
{% endif %}
```

JS

```js title='after.js'
    var script = document.createElement('script');
    script.async = true;
    script.onload = initSakanaWidget;
    script.src = 'https://cdn.jsdelivr.net/npm/sakana-widget@2.7.0/lib/sakana.min.js';

    document.head.appendChild(script);
```