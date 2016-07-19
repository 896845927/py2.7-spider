#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import urllib2


class HtmlDownloader(object):
    def download_html(self, new_url):
        if new_url is None:
            return None
        response = urllib2.urlopen(new_url)
        if response.getcode() != 200:
            return None
        return response.read()