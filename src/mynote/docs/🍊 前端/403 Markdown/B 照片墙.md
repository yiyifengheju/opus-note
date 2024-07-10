---
title: B 照片墙
comments: true
---

```CSS
body {
    width: 60%;
}

.photo-wall {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.photo-wall img {
    width: 100%;
    height: 400px;
    /*padding-bottom: 100%;*/
    object-fit: cover;
}

@media screen and (max-width: 768px) {
    .photo-wall {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    .photo-wall img {
        width: calc(33.33% - 10px);
        height: 400px;
        padding-bottom: calc(33.33% - 10px);
        object-fit: cover;
    }
}
```







```html
<div class="photo-wall">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
</div>
```

<style>

.photo-wall {
display: grid;
grid-template-columns: repeat(3, 1fr);
gap: 10px;
}

.photo-wall img {
width: 100%;
height: 400px;
/*padding-bottom: 100%;*/
object-fit: cover;
}

@media screen and (max-width: 768px) {
.photo-wall {
display: flex;
flex-wrap: wrap;
justify-content: space-between;
}

.photo-wall img {
width: calc(33.33% - 10px);
height: 400px;
padding-bottom: calc(33.33% - 10px);
object-fit: cover;
}
}
</style>

<div class="photo-wall">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fgroup_topic%2Fraw%2Fpublic%2Fp106878681.jpg&refer=http%3A%2F%2Fimg3.doubanio.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671271180&t=13308088bbee45f06884269b6fea239b">
</div>