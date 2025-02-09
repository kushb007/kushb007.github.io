---
layout: page
title: About
permalink: /about/
---

<style>
.centered-card {
  margin: 40px auto;
  max-width: 600px;
  background: #f8f8f8;
  border-radius: 6px;
  text-align: center;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.short-blurb {
  font-size: 1rem;
  margin-top: 10px;
}

.slideshow {
  margin-top: 20px;
  width: 100%;
  overflow: hidden;
  position: relative;
}

.slideshow img {
  width: 100%;
  display: none;
}
</style>

<div class="centered-card">
  <h2>About Me</h2>
  <p class="short-blurb">
    I’m an entry-level software engineer with a passion for clean code and creative solutions.
  </p>

  <div class="slideshow" id="photoSlideshow">
    <img src="https://commons.wikimedia.org/wiki/Main_Page#/media/File:Fischerkirche_(main_door),_Born_a._Dar%C3%9F.jpg" alt="Creative Photo 1" />
    <img src="https://commons.wikimedia.org/wiki/Main_Page#/media/File:Fischerkirche_(main_door),_Born_a._Dar%C3%9F.jpg" alt="Creative Photo 2" />
    <img src="https://commons.wikimedia.org/wiki/Main_Page#/media/File:Fischerkirche_(main_door),_Born_a._Dar%C3%9F.jpg" alt="Creative Photo 3" />
  </div>
</div>

<script type="text/coffeescript">
slides = document.querySelectorAll('#photoSlideshow img')
index = 0

animateSlideshow = ->
  slides[index].style.opacity = 0
  setTimeout ->
    slides[index].style.display = 'none'
    index = (index + 1) % slides.length
    slides[index].style.display = 'block'
    slides[index].style.opacity = 1
  , 1000

setInterval animateSlideshow, 3000

for slide in slides
  slide.style.transition = 'opacity 1s ease-in-out'
  slide.style.opacity = 0

slides[index].style.display = 'block'
slides[index].style.opacity = 1
</script>

This is the base Jekyll theme. You can find out more info about customizing your Jekyll theme, as well as basic Jekyll usage documentation at [jekyllrb.com](https://jekyllrb.com/)

You can find the source code for Minima at GitHub:
[jekyll][jekyll-organization] /
[minima](https://github.com/jekyll/minima)

You can find the source code for Jekyll at GitHub:
[jekyll][jekyll-organization] /
[jekyll](https://github.com/jekyll/jekyll)


[jekyll-organization]: https://github.com/jekyll
