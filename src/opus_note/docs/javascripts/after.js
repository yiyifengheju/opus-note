document$.subscribe(() => {
    // 评论系统
    Waline.init(
        {
            el: '#waline',
            serverURL: 'https://my-notebook-waline-git-main-yiyifengheju.vercel.app/',
            lang: 'zh-CN',
            dark: '[data-md-color-scheme=slate]',
        }
    )

    // 石蒜模拟器
    var script = document.createElement('script');
    script.async = true;
    script.onload = initSakanaWidget;
    script.src = 'https://cdn.jsdelivr.net/npm/sakana-widget@2.7.0/lib/sakana.min.js';

    document.head.appendChild(script);

    // 获取 Vanilla-LazyLoad 实例
    var lazyLoadInstance = new LazyLoad();

    // 调用 update() 方法来强制加载所有元素
    lazyLoadInstance.update();
});