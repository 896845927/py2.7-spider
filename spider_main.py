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

    def craw(self, domain, keyword):
        # http://www.metacritic.com/search/movie/Spider-Man%202/results
        query_url = domain+'/search/movie/'+keyword+'/results'
        query_cont = self.downloader.download_html(query_url)
        results = self.parser.parse_query(query_cont)
        for result in results:
            self.craw_review(domain, result['url']+"/user-reviews?page=0", result['name'])

    def craw_review(self, domain, start_url, movie_name):
        """爬取评论页面"""
        self.urls.add_new_url(start_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                new_url = domain + new_url
                print("new_url:", new_url)
                html_cont = self.downloader.download_html(new_url)
                # with open("html_content.txt","r") as f:
                #     html_cont = f.read()
                new_urls, new_data = self.parser.parse_html(html_cont)
                self.urls.add_new_urls(new_urls)
                self.html_outputer.collect_data(new_data)
            except:
                print "craw fail"
        self.html_outputer.output(movie_name)
