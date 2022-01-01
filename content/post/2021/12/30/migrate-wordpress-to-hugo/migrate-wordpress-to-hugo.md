---
author: Centurio
date: 2021-12-30T19:52:26+01:00
title: Migrate Wordpress to Hugo
description: How I got rid of Wordpress and used Hugo for static content generation
draft: true
---
# Introduction
I'm annoyed by constant update notifications of wordpress. Plugins need also often updates and you've probably read about security issues as well.

## Export from Wordpress
### Plugin
### Wordpress Import in Jekyll
### Jekyll Import in Hugo
Blog posts are put into the `content/post` folder. The filenames are `YYYY-MM-DD-post-title.md`. I recommend changing this to `content/post/YYYY/MM/DD/post-title`, because it will enable cool stuff like image processing. I've created a small python script that moves them automatically.

## Search and replace
* looks interesting: https://gist.github.com/rmaziarka/125cc7dcd99035de971a19dd3c1f46cd#file-wordpress-to-hugo-migrator-js-L288
### Search and replace escaped characters
* replace `&#8230;` with `...`
* replace `&#8222;` with `"`
* replace `"` with `"`
* replace ` ` with ` `
### Search and replace code markups
Wordpress supports code blocks. These should be searched for and be replaced with a suitable markdown replacement.

* replace `<blockquote class="wp-block-quote">` with markdown block
* replace `<blockquote class="twitter-tweet"` with [tweet](https://gohugo.io/content-management/shortcodes/#tweet) shortcode
### Search and replace images
Uploaded files are usually stored in `wordpress/wp-content/uploads` folder. Images are often scaled down for several screen sizes or layout reasons in your blog post. My imported wp-content folder looks like this:

```
hugo-blog/static/wp-content/uploads/2021/02
├── AppleMusicLibrarySelection-261x300.png
├── AppleMusicLibrarySelection-290x290.png
├── AppleMusicLibrarySelection-744x510.png
├── AppleMusicLibrarySelection.png
├── MusicUpdatingLibrary-290x239.png
├── MusicUpdatingLibrary-300x159.png
└── MusicUpdatingLibrary.png
```

So I'll delete every version starting with - after the filename and move them from `static` to [page-bundles](https://gohugo.io/content-management/page-resources/), which is right next to the blog posts. This enables stuff like [image processing](https://gohugo.io/content-management/image-processing/).



## Creating a new post
Use `hugo new posts/hello.md` to create a new blog post. It won't have any additional timestamps in the filename unless you specify it, e.g. like `hugo new posts/2021-12-30-hello.md`. 
### Setup defaults
The start of every markdown blog post contains meta inforamtion describing a blog post. If you'll use the `hugo new` command, it will be pretty empty. That's because there's no default archetype configured. Add this to `archetypes/default.md`:

```
---
author: Your Author Name
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
---
# Introduction
```