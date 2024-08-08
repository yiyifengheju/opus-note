document$.subscribe(() => {
    // 石蒜模拟器
    var script = document.createElement('script');
    script.async = true;
    script.onload = initSakanaWidget;
    script.src = 'https://cdn.jsdelivr.net/npm/sakana-widget@2.7.0/lib/sakana.min.js';

    document.head.appendChild(script);

});