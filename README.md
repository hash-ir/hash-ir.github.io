# Neuralife

Neuralife is the name of my [blog](https://hash-ir.github.io) created with ❤️ using Jekyll and github-pages. I write mostly about academic stuff, sometimes about fictional crossovers and philosophical stories. If you find something interesting on my blog, make sure to ⭐️ this repository so others can know about it.

## Contents
* [Installation](https://github.com/hash-ir/hash-ir.github.io#installation-deployment)
  * [Deployment](https://github.com/hash-ir/hash-ir.github.io#installation-deployment)
  * [Local development](https://github.com/hash-ir/hash-ir.github.io#installation-locally)
* [Usage](https://github.com/hash-ir/hash-ir.github.io#usage)
* [Features](https://github.com/hash-ir/hash-ir.github.io#features)
* [Contributing](https://github.com/hash-ir/hash-ir.github.io#contributing)
* [Credits](https://github.com/hash-ir/hash-ir.github.io#credits)
* [License](https://github.com/hash-ir/hash-ir.github.io#license)

## Installation (deployment)
With this, you will be able to use the features and create new posts only. Local development and live review is not possible:
1. Sign Up for a GitHub account if you don't have one.
2. For a minimal installation, fork the original lanyon [repository](https://github.com/poole/lanyon) by clicking the "Fork" button in the top right. Otherwise, for additional features, fork this repository.
3. Go to your forked repository settings. Rename the repository to [username].github.io.
4. Set site-wide configuration by editing the *_config.yml* file. You can set the blog title, description, author and other meta features. Have a look [here](https://github.com/hash-ir/hash-ir.github.io/blob/master/_config.yml). 
5. Check status of your deployment in the repository settings under "GitHub Pages" section. You should be seeing a green tick with the message "Your site is published at https://[username].github.io/"

## Installation (locally)
With this, you can locally run the jekyll site, preview posts and add new features or plugins:
1. Clone the forked repository after doing the steps above.
2. Install ruby, ruby-gems, jekyll and other dependencies from [here](https://jekyllrb.com/docs/installation/).
3. The plugins used in the site are listed in both *_config.yml* and *Gemfile*. Run `bundle clean` followed by `bundle install` to install the plugins. If there is any error, delete *Gemfile.lock* and try again.
4. In the repository directory, run `jekyll serve`. If everything works correctly, you will be able to see the local deployment at http://127.0.0.1:4000/ or http://localhost:4000/.
5. If you want to use livereload of pages, run `jekyll serve --livereload`. As per the documentation, livereload is built into Jekyll 3.7+. If it doesn't work, make sure `jekyll-paginate` is listed in *_config.yml* in the following manner:
```html
plugins:
 - jekyll-paginate
```
Then do the following:
```bash
gem install jekyll-paginate
gem uninstall eventmachine
gem install eventmachine --platform ruby -- --use-system-libraries --with-ssl-dir=C:/Ruby26-x64/msys64/mingw64
ruby -reventmachine -e "puts EM.ssl?"  => true
```
Replace `--with-ssl-dir` path with your installation of MinGW64. If you installed Ruby with all the development tools, it will be in the Ruby installation directory like above. After that, run `jekyll serve --livereload`.

## Usage
This is really simple. You can create posts as markdown files in *_posts* directory. The posts are chronologically ordered based on their name. The name follows the convention `YYYY-MM-DD-name-of-the-post.md`. The name of the file becomes the url (https://[username].github.io/YYYY/MM/DD/name-of-the-post/) when the html is rendered. Inside the markdown file, there should be a frontmatter section (between `---` and `---`) at the top. This section describes the meta information about the post (layout, title, author etc) and is rendered based on the layout described in the Jekyll theme you are using. For example:
```html
---
layout: post
title: My Awesome Post
author: John Doe
---
```
You can also create post drafts which will not be rendered when your site is published. These should be created in a separate directory *_drafts*. The drafts are also markdown files and should have the frontmatter at the top. You can name the drafts anything you like until you move them to the *_posts* directory. The drafts can be previewed locally by running `jekyll serve --livereload --drafts`.

## Features
I have used [Lanyon](https://lanyon.getpoole.com/), a minimalistic jekyll theme. The following features have been added which make this blog exceedingly amazing. The detailed guides are available in the Wiki
1. Disqus comments (June 10, 2020)
2. Author name and post excerpt (June 15, 2020)
3. Google Analytics (July 7, 2020)
4. Categorization of posts by tags (August 20, 2020)
5. MathJax support for math expressions (August 20, 2020)
6. Link preview using `jekyll-seo-tag` (September 4, 2020)
7. Create drafts of posts without publishing (September 4, 2020)


## Contributing
[TODO]

## Credits
[TODO]

## License
The license is extended from the source [repository](https://github.com/poole/lanyon). See the license [file](https://github.com/hash-ir/hash-ir.github.io/blob/master/LICENSE.md) for details.
