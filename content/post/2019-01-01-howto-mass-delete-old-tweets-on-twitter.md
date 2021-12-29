---
author: Centurio
categories:
- Internet und co
date: "2019-01-01T20:44:58Z"
guid: http://centurio.net/?p=3248
id: 3248
tags:
- CleanUp
- Twitter
title: Howto mass delete old Tweets on Twitter
url: /2019/01/01/howto-mass-delete-old-tweets-on-twitter/
---
There's unfortunately no way to mass delete old Tweets you've posted on Twitter. There are some online services, who promise to delete your data for you, but since you'll have to grant them access to your account I've got a bad feeling and wanted to do things on my own.

I've tried last year a windows only software called [Twitter Archive Eraser](https://martani.github.io/Twitter-Archive-Eraser/). Last year it used to be a github project which you could compile locally and let it run on your account. It's now free for a limited amount of tweets and also only works with tweets not older than two years. To remove these restrictions you've got to pay a small amount for a license.

You'll need to download your complete message archive for the deletion process. Once you've got the data from Twitter you might as well start to write a little script which deletes the old messages for you using the Twitter post id. 

Luckily, I found [this blog post by Kris Shaffer](https://pushpullfork.com/i-deleted-tweets/). He explains how he deleted a large amount of his tweets using python so I've started to try this for myself.

## New approach using JSON Twitter archives

This is the currently working approach (December 2020). I've updated the python script accordingly and put it into its separate [git repo on GitHub](https://github.com/rudelm/tweetcleaner).

## Old approach using CVS Twitter archives

There was also a different blog which explained the process more [beginner friendly](http://digitallearning.middcreate.net/tips/deleting-tweets-non-techie-starts-her-personal-information-environmentalism-journey-with-lots-of-help/). However, I've got problems with misformatted characters so I've decided to post my used code as gist to github:

To use this I've done the following things:

  * Requested and download my account data from Twitter
  * Create a Twitter developer account
  * Created a new app to get Api keys and Access tokens
  * Installed python3 on my mac with homebrew &#8218;brew install python3&#8216;
  * Installed tweepy with pip3 &#8218;pip3 install tweepy&#8216;
  * Created a [virtual environment](https://wsvincent.com/install-python3-mac/) for this script
  * Copied the lines in blocks into the python3 interactive shell

Please be aware that above gist only deleted the tweets from 2017 to June 2018. Please refer for other scenarios to Kris blog post (e.g. delete only mentions in a given time frame).