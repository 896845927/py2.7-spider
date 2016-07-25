#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from threading import Thread
from spider_main import Spider


class CrawThread(Thread):
    def __init__(self, domain, keyword):
        self.domain = domain
        self.keyword = keyword
        super(CrawThread, self).__init__()

    def run(self):
        spider = Spider()
        spider.craw(self.domain, self.keyword)