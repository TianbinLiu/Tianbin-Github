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

***

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

***

## Week 3
### HTML Code [navigation.html](https://github.com/TianbinLiu/TianbinLiu.github.io/blob/github_pages/_includes/navigation.html)

```html
<!-- add more option on menu and change menu into muti-level menu-->
<ul id="nav">
        <li><a href="/.">Home</a></li>
        <li><a href="/collegeboard">Collegeboard Notes</a>
            <ul>
                <li><a href="/5.1">5.1</a></li>
                <li><a href="/5.2">5.2</a></li>
                <li><a href="/5.3">5.3</a></li>
                <li><a href="/5.4">5.4</a></li>
                <li><a href="/5.5">5.5</a></li>
                <li><a href="/5.6">5.6</a></li>
            </ul>
        </li>
    </ul>
```

### CSS Code [navigation.html](https://github.com/TianbinLiu/TianbinLiu.github.io/blob/github_pages/_includes/navigation.html)

```html
<!-- add css-->
<style>
        #nav {
            list-style: none inside;
            margin: 0;
            padding: 0;
            text-align: center;
        }

        #nav li {
            display: block;
            position: relative;
            float: left;
            background: rgb(255,255,255); 
            /* menu background color */
        }

        #nav li a {
            display: block;
            padding: 0;
            text-decoration: none;
            width: 130px;
            /* this is the width of the menu items */
            line-height: 35px;
            /* this is the hieght of the menu items */
            color: rgb(0,0,0);
            /* list item font color */
        }
        

        #nav li li a {
            font-size: 80%;
        }

        /* smaller font size for sub menu items */

        #nav li:hover {
            background: #D1D1D1;
        }

        /* highlights current hovered list item and the parent list items when hovering over sub menues */

        #nav ul {
            position: absolute;
            padding: 0;
            left: 0;
            display: none;
            /* hides sublists */
        }

        #nav li:hover ul ul {
            display: none;
        }

        /* hides sub-sublists */

        #nav li:hover ul {
            display: block;
        }

        /* shows sublist on hover */

        #nav li li:hover ul {
            display: block;
            /* shows sub-sublist on hover */
            margin-left: 130px;
            /* this should be the same width as the parent list item */
            margin-top: -35px;
            /* aligns top of sub menu with top of list item */
        }
</style>
```

***

## Week 4
### HTML Code [gmap.html](https://github.com/vaishavijay/pain.github.io/blob/main/templates/gmap.html)

```html
<!-- add google map page into team project -->
{% extends "layout.html" %}

{% block meta %}
<title>Google Map</title>
{% endblock %}

{% block content %}
<style>
    h1 {
        width: 576px;
        height: 94px;

        font-family: 'Righteous';
        font-style: normal;
        font-weight: 400;
        font-size: 60px;
        line-height: 75px;

        color: #9C9C9C;
    }
    button {
        width: 180px;
        height: 45px;

        background: #6886A1;
        border-radius: 24px;

        font-family: 'Heebo';
        font-style: normal;
        font-weight: 400;
        font-size: 24px;
        line-height: 35px;

        color: #E5E5E5;

    }


</style>

<center>
    <h1>
        Therapist Near You
    </h1>

    <button type="button" onclick="window.location.href='https://www.google.com/maps/place/Elevate+Therapy+Psychological+Services/@33.0283195,-117.1146981,15z/data=!3m1!5s0x80dbf72bafaeaa3d:0x431aa384c6b17370!4m9!1m2!2m1!1stherapist!3m5!1s0x80dbf7ebcc49535d:0x8c7b093b5bf7d9be!8m2!3d33.0223892!4d-117.0828559!15sCgl0aGVyYXBpc3RaCyIJdGhlcmFwaXN0kgEMcHN5Y2hvbG9naXN0mgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVU00YlRZeVJHdG5SUkFC'"  >Therapist #1</button>
    <button type="button" onclick="window.location.href='https://www.google.com/maps/place/Positive+Change+Counseling+Center/@33.0283195,-117.1146981,15z/data=!3m1!5s0x80dbf72c9e3c5567:0x19389120001bd292!4m9!1m2!2m1!1stherapist!3m5!1s0x80dbf7628ead2f21:0x76548fa85436153a!8m2!3d33.02059!4d-117.0812184!15sCgl0aGVyYXBpc3RaCyIJdGhlcmFwaXN0kgEUbWVudGFsX2hlYWx0aF9jbGluaWOaASRDaGREU1VoTk1HOW5TMFZKUTBGblNVTTJOR1JYTTNwblJSQUI'"  >Therapist #2</button>
    <button type="button" onclick="window.location.href='https://www.google.com/maps/place/Deborah+Moyer,+LMFT/@33.0283195,-117.1146981,15z/data=!3m1!5s0x80dbf72bafaeaa3d:0x431aa384c6b17370!4m9!1m2!2m1!1stherapist!3m5!1s0x80dbf72ba6964af7:0x24237324143c33c6!8m2!3d33.0218296!4d-117.0826598!15sCgl0aGVyYXBpc3SSAQljb3Vuc2Vsb3I'"  >Therapist #3</button>
    <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d13381.121730992692!2d-117.13691915!3d33.02274155!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1649547417678!5m2!1sen!2sus"  width="1500" height="700" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</center>



{% endblock %}
```

### HTML Code [cruddy](https://github.com/vaishavijay/pain.github.io/tree/main/cruddy)

```html
<!-- add login into google map page -->
@app_crud.route('/mlogin/', methods=["GET", "POST"])
def crud_mlogin():
    # obtains form inputs and fulfills login requirements
    if request.form:
        email = request.form.get("email")
        password = request.form.get("password")
        if login(email, password):       # zero index [0] used as email is a tuple
            return redirect(url_for('gmap'))

    # if not logged in, show the login page
    return render_template("mlogin.html")

@app_crud.route("/logout")
@login_required
def logout():
    logout()
    return render_template("index.html")
```

***

## Week 5
### HTML Code [test.md](https://github.com/TianbinLiu/TianbinLiu.github.io/blob/github_pages/test.md)

```html
<!-- add more collegeboard notes -->
<table>
   <tr>
    <th>AP Testers</th>
   </tr>
   
   <tr>
    <td><a href="https://github.com/TianbinLiu/Tianbin-Github/wiki/AP-Testers#finals-quiz1-score4350-and-corrections">Finals-Quiz1 score 43/50 and corrections</a></td>
   </tr>

  
   <tr>
    <td><a href="https://github.com/TianbinLiu/Tianbin-Github/wiki/AP-Testers#finals-quiz2-score4650-and-corrections">Finals-Quiz2 score 46/50 and corrections</a></td>
   </tr>
```

### HTML Code [navigation.html](https://github.com/TianbinLiu/TianbinLiu.github.io/blob/github_pages/_includes/navigation.html)

```html
<!-- add study plan -->
<table>
   <tr>
    <th>Study Plan</th>
   </tr>
   
   <tr>
    <td><a href="https://github.com/TianbinLiu/Tianbin-Github/wiki/Study-Plan#:~:text=Plan/To%20Do-,4,-Monday">Week 4</a></td>
   </tr>
   
   <tr>
    <td><a href="https://github.com/TianbinLiu/Tianbin-Github/wiki/Study-Plan#:~:text=Friday-,5,-Monday">Week 5</a></td>
   </tr>
  
   <tr>
    <td><a href="https://github.com/TianbinLiu/Tianbin-Github/wiki/Study-Plan#:~:text=Friday-,6,-Monday">Week 6</a></td>
   </tr>
  
   <tr>
    <td><a href="https://github.com/TianbinLiu/Tianbin-Github/wiki/Study-Plan#:~:text=Friday-,7,-Monday">Week 7</a></td>
   </tr>
```
