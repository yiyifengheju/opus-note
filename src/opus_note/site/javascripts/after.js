document$.subscribe(() => {
    // 评论系统================================================
    Waline.init(
        {
            el: '#waline',
            serverURL: 'https://my-notebook-waline-git-main-yiyifengheju.vercel.app/',
            lang: 'zh-CN',
            dark: '[data-md-color-scheme=slate]',
        }
    )
    // END====================================================

    // 石蒜模拟器====================================================
    var script = document.createElement('script');
    script.async = true;
    script.onload = initSakanaWidget;
    script.src = 'https://cdn.jsdelivr.net/npm/sakana-widget@2.7.0/lib/sakana.min.js';
    document.head.appendChild(script);
    // END====================================================

    // Vanilla图片懒加载================================================
    var lazyLoadInstance = new LazyLoad();
    lazyLoadInstance.update();
    // END====================================================

    // 动态加载fireworks================================================
    // setCanvasSize();
    // END====================================================

    // Lightbox重新加载================================================
    lightbox.reload();

    var script2 = document.createElement('script');
    script2.async = false;
    script2.onload = setCanvasSize;
    script2.src = '/javascripts/fireworks.min.js';
    document.head.appendChild(script2);
    // END====================================================
});