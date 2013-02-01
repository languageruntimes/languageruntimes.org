#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Bruce Mitchener, Jr."
SITENAME = u"Language Runtimes"
SITEURL = 'http://languageruntimes.org'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

DEFAULT_CATEGORY = 'General'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Pages
PAGES = (('About', '/about/'),
	     ('Ideas', '/ideas/'),
         ('Get Involved', '/get-involved/'))

# Blogroll
LINKS =  (('Lambda the Ultimate', 'http://lambda-the-ultimate.org/'),
	      ('Dylan Foundry', 'http://dylanfoundry.org/'))

# Social widget
SOCIAL = (('icon-github', 'GitHub', 'https://github.com/languageruntimes/'),)

GITHUB_URL = 'https://github.com/languageruntimes/'
TWITTER_USERNAME = 'LangRuntimes'
# DISQUS_SITENAME = 'languageruntimes'

DEFAULT_PAGINATION = 10

SUMMARY_MAX_LENGTH = None

THEME = 'theme'
