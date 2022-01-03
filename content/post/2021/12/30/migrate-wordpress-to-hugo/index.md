---
author: Centurio
date: 2021-12-30T19:52:26+01:00
title: Migrate Wordpress to Hugo
description: How I got rid of Wordpress and used Hugo for static content generation
categories:
- Blogs
tags:
- Hugo
draft: true
---
# Introduction
I'm annoyed by constant update notifications of wordpress. Plugins need also often updates and you've probably read about security issues as well.

## Export from Wordpress
### Plugin
### Wordpress Import in Jekyll
### Jekyll Import in Hugo
Blog posts are put into the `content/post` folder. The filenames are `YYYY-MM-DD-post-title.md`. I recommend changing this to `content/post/YYYY/MM/DD/post-title`, because it will enable cool stuff like image processing. I've created a small python script that moves them automatically called `rename-posts.py`.

## Search and replace
* looks interesting: https://gist.github.com/rmaziarka/125cc7dcd99035de971a19dd3c1f46cd#file-wordpress-to-hugo-migrator-js-L288
### Search and replace escaped characters
* replace `&#8230;` with `...`
* replace `&#8222;` with `"`
* replace `&#8220;` with `"`
* replace `&nbsp;` with ` `
### Search and replace code markups
Wordpress supports code blocks. These should be searched for and be replaced with a suitable markdown replacement.

* replace `<blockquote class="wp-block-quote">` with markdown block
* replace `<blockquote class="twitter-tweet"` with [tweet](https://gohugo.io/content-management/shortcodes/#tweet) shortcode

### Search images
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

So I'll delete every version starting with - after the filename or `.thumbnail` and moved them manually (because of the few occurences) from `static` to [page-bundles](https://gohugo.io/content-management/page-resources/), which is right next to the blog posts. This enables stuff like [image processing](https://gohugo.io/content-management/image-processing/).

The references to the moved images need then an update in the blog post md file. This is now depending on the way how you've originally added the image to the blog post and won't be part of this post.

Additionally, there were a few images I had to check manually because of cryptic filenames. Those were probably used in blog posts, which I've already deleted. Wordpress doesn't automatically cleanup the linked media. However, these files might also come from the wordpress conversion. They look like duplicates, which I've decided to remove by using a tool called `jdupes`. Install it with `brew install jdupes` and execute it with `jdupes -r -d -N -X onlyext:png,jpg,gif .` inside the hugo root. It will show you a list of duplicates that should help with identifying duplicate files.

`-r` is recursive
`-d` is delete - asks for each entry it found
`-N` is no prompt when used with `-d` and keeps the first found occurence
`-X onlyext:png,jpg,gif` is to filter only for images with these endings

```
   [+] ./static/wp-content/uploads/2013/05/92b42fc0dd77937dab3f1fc69c11612c.jpg
   [-] ./static/wp-content/uploads/2013/05/fc635790673962f16d9e10363c4e5ad8.jpg
   [-] ./static/wp-content/uploads/2013/06/92b42fc0dd77937dab3f1fc69c11612c.jpg
   [-] ./static/wp-content/uploads/2013/06/fc635790673962f16d9e10363c4e5ad8.jpg
   [-] ./static/wp-content/uploads/2013/07/92b42fc0dd77937dab3f1fc69c11612c.jpg
   [-] ./static/wp-content/uploads/2013/07/b4f7e989575cb39b56455cef9a63aec4.jpg
   [-] ./static/wp-content/uploads/2013/07/fc635790673962f16d9e10363c4e5ad8.jpg
   [-] ./static/wp-content/uploads/2013/08/92b42fc0dd77937dab3f1fc69c11612c.jpg
   [-] ./static/wp-content/uploads/2013/08/fc635790673962f16d9e10363c4e5ad8.jpg
   [-] ./static/wp-content/uploads/2013/09/92b42fc0dd77937dab3f1fc69c11612c.jpg
   [-] ./static/wp-content/uploads/2013/09/fc635790673962f16d9e10363c4e5ad8.jpg
   [-] ./static/wp-content/uploads/2013/10/92b42fc0dd77937dab3f1fc69c11612c.jpg
   [-] ./static/wp-content/uploads/2013/10/fc635790673962f16d9e10363c4e5ad8.jpg
   [-] ./static/wp-content/uploads/2013/11/92b42fc0dd77937dab3f1fc69c11612c.jpg
   [-] ./static/wp-content/uploads/2013/11/fc635790673962f16d9e10363c4e5ad8.jpg


   [+] ./static/wp-content/uploads/2013/03/f6b58f2ba979ce0e3e176083c9fc3782.gif
   [-] ./static/wp-content/uploads/2013/04/f6b58f2ba979ce0e3e176083c9fc3782.gif


   [+] ./static/wp-content/uploads/2013/03/5027a0330756c412c0b0116e0cdbc939.jpg
   [-] ./static/wp-content/uploads/2013/04/5027a0330756c412c0b0116e0cdbc939.jpg
```

After this there were still a lot of cryptic looking files. Many of them still look like a duplicate according to their filename, but not to their file size:

```
-rw-r--r--   1 rudelm  staff   25486  3 Jan 00:33 022010c8d0cf8bd34ad58b051628d1d9.jpg
-rw-r--r--   1 rudelm  staff   25486  3 Jan 00:33 0703c65ee7cdab74b94f665b78366d14.jpg
-rw-r--r--   1 rudelm  staff   25486  3 Jan 00:33 1963042489e86ef304437d3345e628da.jpg
```

vs

```
-rw-r--r--   1 rudelm  staff   25109  3 Jan 00:33 022010c8d0cf8bd34ad58b051628d1d9.jpg
-rw-r--r--   1 rudelm  staff   25109  3 Jan 00:33 0703c65ee7cdab74b94f665b78366d14.jpg
-rw-r--r--   1 rudelm  staff   25109  3 Jan 00:33 1963042489e86ef304437d3345e628da.jpg
```

I've removed those files manually as I did not find a good working way to detect those duplicates just based on their filenames. I would have expected something like this from `jdupes` when its started with `-Q` which disables a lot of checks but without a chance.

### Replace images
If all images are moved to next to the blog post as part of a page resource, it can be now referenced in the markdown by [using a shortcode](https://www.regisphilibert.com/blog/2018/01/hugo-page-resources-and-how-to-use-them/). Here's my `img.html` since the linked had a small bug and did not show the figure caption:

```html
{{ $img := $.Page.Resources.GetMatch (.Get 0)}}
<figure>
	<img src="{{ $img.RelPermalink }}" alt="{{(.Get 1)}}" />
	<figcaption>{{(.Get 1)}}</figcaption>
</figure>
```

### Remove empty folders
The Jekyll import contained a lot of empty folders in `static/wp-content/uploads` which I've cleaned by using `find ./static -type d -empty -delete`

### Remove unused folders
I've got some folders which where created by a plugin. They can all be deleted, e.g. `static/wp-content/backupwp-*` or `static/wp-content/thumb-cache`.

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