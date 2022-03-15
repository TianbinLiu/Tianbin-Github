---
title: code
---

<div id="video_wrapper">
  <video autoplay loop>
    <source src="https://drive.google.com/uc?export=view&id=1Qote5m--Bme0bE4_o6wAKNRxWY8pJnuL" type="video/mp4">
  </video>
</div>
##Week 0

* HTML Code [index.md](https://github.com/TianbinLiu/Tianbin-Github/edit/main/index.md)

```html
<!-- added to file that need video background-->
<div id="video_wrapper">
  <video autoplay loop>
    <source src="https://drive.google.com/uc?export=view&id=1Qote5m--Bme0bE4_o6wAKNRxWY8pJnuL" type="video/mp4">
  </video>
</div>
```

* CSS Code [head-custom2.html](https://github.com/TianbinLiu/Tianbin-Github/edit/main/_includes/head-custom2.html)

```html
<!-- CSS in head-custom2.html added into layouts-->
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

* CSS added into layout to apply the whole GitHub Page [default.html](https://github.com/TianbinLiu/Tianbin-Github/edit/main/_layouts/default.html)

```html
{% include navigation.html %}
```

* Menu [navigation.html](https://github.com/TianbinLiu/Tianbin-Github/edit/main/_includes/navigation.html)

```html
<!-- added to file that need video background-->
 <table>
     <tr>
         <td><a href=".">Home</a></td>
         <td><a href="collegeboard">Collegeboard video</a></td>
         <td><a href="replit">Replit menu</a></td>
         <td><a href="create">Create task project</a></td>
         <td><a href="code">Code</a></td>
     </tr>
 </table>
 <hr>
```
