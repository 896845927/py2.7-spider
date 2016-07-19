#!/usr/bin/env python
# _*_ coding: utf-8 _*_
class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is not None and url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        if len(self.new_urls) > 0:
            return True

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_urls(self, new_urls):
        if new_urls is not None and len(new_urls)>0:
            for url in new_urls:
                self.add_new_url(url)