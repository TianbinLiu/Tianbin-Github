---
title: code
---

<div id="video_wrapper">
  <video autoplay loop>
    <source src="https://drive.google.com/uc?export=view&id=1Qote5m--Bme0bE4_o6wAKNRxWY8pJnuL" type="video/mp4">
  </video>
</div>
##Week 0

* HTML Code [head-custom2.html](https://github.com/TianbinLiu/Tianbin-Github/edit/main/_includes/head-custom2.html)

```html
<!-- added to file that need video background-->
<div id="video_wrapper">
  <video autoplay loop>
    <source src="https://drive.google.com/uc?export=view&id=1Qote5m--Bme0bE4_o6wAKNRxWY8pJnuL" type="video/mp4">
  </video>
</div>
```

* CSS Code [index.md](https://github.com/TianbinLiu/Tianbin-Github/edit/main/index.md)

```html
<!-- added to file that need video background-->
<style>
#video_wrapper {
    margin:0px;
    padding:0px;
}
#video_wrapper video {
    position: fixed;
    top: 50%; left: 50%;
    z-index: -99; important!
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    transform: translate(-50%, -50%);
}
</style>
```
