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

    // 动态加载fireworks
    window.human=false;var canvasEl=document.querySelector(".fireworks");var ctx=canvasEl.getContext("2d");var numberOfParticules=30;var pointerX=0;var pointerY=0;var tap="ontouchstart"in window||navigator.msMaxTouchPoints?"touchstart":"mousedown";var colors=["#FF1461","#18FF92","#5A87FF","#FBF38C"];function setCanvasSize(){canvasEl.width=window.innerWidth*2;canvasEl.height=window.innerHeight*2;canvasEl.style.width=window.innerWidth+"px";canvasEl.style.height=window.innerHeight+"px";canvasEl.getContext("2d").scale(2,2)}function updateCoords(e){pointerX=e.clientX||e.touches[0].clientX;pointerY=e.clientY||e.touches[0].clientY}function setParticuleDirection(p){var angle=anime.random(0,360)*Math.PI/180;var value=anime.random(50,180);var radius=[-1,1][anime.random(0,1)]*value;return{x:p.x+radius*Math.cos(angle),y:p.y+radius*Math.sin(angle)}}function createParticule(x,y){var p={};p.x=x;p.y=y;p.color=colors[anime.random(0,colors.length-1)];p.radius=anime.random(16,32);p.endPos=setParticuleDirection(p);p.draw=function(){ctx.beginPath();ctx.arc(p.x,p.y,p.radius,0,2*Math.PI,true);ctx.fillStyle=p.color;ctx.fill()};return p}function createCircle(x,y){var p={};p.x=x;p.y=y;p.color="#FFF";p.radius=.1;p.alpha=.5;p.lineWidth=6;p.draw=function(){ctx.globalAlpha=p.alpha;ctx.beginPath();ctx.arc(p.x,p.y,p.radius,0,2*Math.PI,true);ctx.lineWidth=p.lineWidth;ctx.strokeStyle=p.color;ctx.stroke();ctx.globalAlpha=1};return p}function renderParticule(anim){for(var i=0;i<anim.animatables.length;i++){anim.animatables[i].target.draw()}}function animateParticules(x,y){var particules=[];for(var i=0;i<numberOfParticules;i++){particules.push(createParticule(x,y))}anime.timeline().add({targets:particules,x:function(p){return p.endPos.x},y:function(p){return p.endPos.y},radius:.1,duration:anime.random(1200,1800),easing:"easeOutExpo",update:renderParticule})}var render=anime({duration:Infinity,update:function(){ctx.clearRect(0,0,canvasEl.width,canvasEl.height)}});document.addEventListener(tap,function(e){window.human=true;updateCoords(e);animateParticules(pointerX,pointerY)},false);var centerX=window.innerWidth/2;var centerY=window.innerHeight/2;setCanvasSize();

});