---
title: code
---

<div id="video_wrapper">
  <video autoplay loop>
    <source src="https://drive.google.com/uc?export=view&id=1lDrbQtLYGj79HjdD-icfLel9xTnVn-T7" type="video/mp4">
  </video>
</div>

## Week 0

### HTML Code [index.md](https://github.com/TianbinLiu/Tianbin-Github/edit/main/index.md)

```html
<!-- added to file that need video background-->
<div id="video_wrapper">
  <video autoplay loop>
    <source src="https://drive.google.com/uc?export=view&id=1Qote5m--Bme0bE4_o6wAKNRxWY8pJnuL" type="video/mp4">
  </video>
</div>
```

### CSS Code [head-custom2.html](https://github.com/TianbinLiu/Tianbin-Github/edit/main/_includes/head-custom2.html)

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

### CSS added into layout to apply the whole GitHub Page [default.html](https://github.com/TianbinLiu/Tianbin-Github/edit/main/_layouts/default.html)

```html
{% include navigation.html %}
```

### Menu [navigation.html](https://github.com/TianbinLiu/Tianbin-Github/edit/main/_includes/navigation.html)

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

## Week 1
### HTML Code [default.html](https://github.com/TianbinLiu/Tianbin-Github/blob/main/_layouts/default.html)

```html
<!-- added layout and apply to GitHub page-->
    <link rel="stylesheet" href="{{ '/assets/css/style.css?v=' | append: site.github.build_revision | relative_url }}">
    <script src="https://code.jquery.com/jquery-1.12.4.min.js" integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=" crossorigin="anonymous"></script>
    <script src="{{ '/assets/js/respond.js' | relative_url }}"></script>
    <!--[if lt IE 9]>
      <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <!--[if lt IE 8]>
    <link rel="stylesheet" href="{{ '/assets/css/ie.css' | relative_url }}">
    <![endif]-->
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
    {% include head-custom.html %}
    
    <!-- nighthawk coding society has inserted its own file for thigs like <style>-->
    {% include head-custom2.html %}

  </head>
```

### CSS Code [head-custom2.html](https://github.com/TianbinLiu/Tianbin-Github/blob/main/_includes/head-custom2.html)

```html
<!-- moved css to that page-->
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
