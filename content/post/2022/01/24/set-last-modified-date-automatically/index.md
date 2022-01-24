---
author: Centurio
title: "Set Last Modified Date Automatically"
date: 2022-01-24T20:14:14+01:00
categories:
- Blogs
tags:
- Hugo
---
# Introduction
I've wanted to see when a blog post was last updated. My current Hugo theme doesn't offer support for this. Luckily I found [this blog post](https://makewithhugo.com/add-a-last-edited-date/) and modified it to my needs.

## Changes to config.yaml
Since I don't have everywhere in the frontmatter a `lastmod` value, I need to rely on the git timestamp. I have to modify the `config.yaml` so that Hugo can use this information. In case I've added the `lastmod` manually, it should override the information from git:

```
enableGitInfo: true

frontmatter:
  lastmod: ['lastmod', ':git', 'date', 'publishDate']
```

## Modify the theme
Existing files from a theme [can be overridden](https://gohugobrasil.netlify.app/themes/customizing/). You'll need to copy the existing file to the same place in your `layouts` folder. I've added these changes to my `details.html`:

```
{{ if or (not .Date.IsZero) (.Site.Params.article.readingTime) }}
    <footer class="article-time">
        {{ if not .Date.IsZero }}
            <div>
                {{ partial "helper/icon" "date" }}
                <time class="article-time--published">
                    {{- .Date.Format (or .Site.Params.dateFormat.published "Jan 02, 2006") -}}
                </time>
            </div>
        {{ end }}

        <!-- Created Date -->
        {{- $pubdate := .PublishDate.Format "Jan 02, 2006" }}
        <!-- Last Updated Date -->
        {{- if .Lastmod }}
            {{- $lastmod := .Lastmod.Format "Jan 02, 2006" }}
                {{- if ne $lastmod $pubdate }}
                    Last modified:
                    <time class="article-time--updated" datetime="{{ .Lastmod }}" title="{{ .Lastmod }}">
                        {{ $lastmod }}
                    </time>
            {{- end }}
        {{- end }}

        {{ if .Site.Params.article.readingTime }}
            <div>
                {{ partial "helper/icon" "clock" }}
                <time class="article-time--reading">
                    {{ T "article.readingTime" .ReadingTime }}
                </time>
            </div>
        {{ end }}
    </footer>
```

# Conclusion
Now you'll see in lot of my posts a "Last modified" next to the published date.  I've updated almost all my posts, as they were recently modified to be compatible with Hugo.