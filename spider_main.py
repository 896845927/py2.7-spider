#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import html_downloader
import html_outputer
import html_parser
import url_manager


class Spider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.html_outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, main_url):
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download_html(new_url)
                new_urls, new_data = self.parser.parse_html(main_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.html_outputer.collect_data(new_data)
            except:
                print "craw fail"
        self.html_outputer.output()

if __name__ == "__main__":
    root_url = "http://www.metacritic.com/movie/spider-man-3/user-reviews"
    spider = Spider()
    spider.craw(root_url, 'http://www.metacritic.com/')
