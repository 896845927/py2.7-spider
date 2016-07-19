#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from bs4 import BeautifulSoup
import re


class HtmlParser(object):
    def __init__(self):
        self.new_urls = set()
        self.new_datas = []

    def parse_html(self, main_url, html_cont):
        if main_url is None or html_cont is None or len(html_cont)==0:
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding='utf-8')
        self.parse_new_urls(soup)
        self.parse_new_datas(soup)
        return self.new_urls, self.new_datas
    def parse_new_urls(self, soup):
        links = soup.find_all('a', class_='page_num', href=re.compile(r"user-reviews\?page=\d$"))
        self.new_urls = set(links)

    def parse_new_datas(self, soup):
        names = soup.select(".name > span")
        scores = soup.select(".review_grade > .user")
        dates = soup.select(".review_critic > .date")
        user_reviews = []
        html_user_reviews = soup.select(".review_body > span")
        for review in html_user_reviews:
            user_reviews.append(review.select(".blurb_expanded")[0].string if review.string == None else review.string)
        for n, s, d, rw in zip(names, scores, dates, user_reviews):
            self.new_datas.append([n.string, s.string, d.string, rw])