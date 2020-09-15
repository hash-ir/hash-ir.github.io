# Neuralife

Neuralife is the name of my [blog](https://hash-ir.github.io) created with ❤️ using Jekyll and github-pages. I write mostly about academic stuff, sometimes about fictional crossovers and philosophical stories. If you find something interesting on my blog, make sure to ⭐️ this repository so others can know about it. 

## Features
I have used [Lanyon](https://lanyon.getpoole.com/), a minimalistic jekyll theme. I also added the following features on top which make this blog exceedingly amazing: 
### Disqus comments (June 10, 2020)
Sign up at [Disqus](https://disqus.com/). Go to settings and select *Add Disqus to Site*. Enter the site name and other details. Finally, select *Universal Code* as your platform. Save the universal code given under comment box. 

In `post.html` after the post content or where ever you want to display the comments, add the following:
```html
{% if page.comments %}
  <h2>Comments</h2>
  {% include disqus.html%}
{% endif %}
```
The `if` logic only displays comments when they are turned on in the frontmatter (shown below). Now, create an html file `disqus.html` and a javascript file `disqus.js`. Add the following lines to `disqus.html`:
```html
<div id="disqus_thread"></div>
  <script src="/public/js/disqus.js"></script>
  <noscript>
    Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a>
  </noscript>
```
In `disqus.js`, paste the universal code from before. For a post to display the comments, add the following in the post frontmatter.
```html
comments: true
```
If everything goes well, you will see something like this below your post:

<img src="public/images/comments.PNG" alt="comments-box" width="600px" />

### Author name and post excerpt (June 15, 2020)
This looks like below:

<img src="public/images/author-excerpt.png" alt="author-excerpt" width="600px" />

It can be done easily using Jekyll's Liquid templating. In order to display the author's name and excerpt on the post page as well as on the home page, we have to modify `post.html` and `index.html`. In the `<div class="post">` element of both files, add the following under `page.date` (`post.date` in `index.html`) variable:
```html
{% if page.author %}
  | {{ page.author }}
{% endif %}
```
The `author` variable is added in the post frontmatter as below:
```html
author: John Doe
```
For the post excerpt, we modify only the `index.html` and add `{{ post.excerpt }}` under author information. You can also add a *Read More...* hyperlink which opens the post page:
```html
<a href="{{ post.url | absolute_url }}">Read more...</a>
```
### Google Analytics (July 7, 2020)
### Categorization of posts by tags (August 20, 2020)
### MathJax support for math expressions (August 20, 2020)
### Link preview using `jekyll-seo-tag` (September 4, 2020) - *needs improvement*
### Create drafts of posts without publishing (September 4, 2020)

I will update the readme with a detailed guide about each feature!
