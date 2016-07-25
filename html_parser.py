#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from bs4 import BeautifulSoup
import re


class HtmlParser(object):

    def parse_query(self, html_cont):
        """解析关键字搜索结果"""
        if html_cont is None or len(html_cont) == 0:
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding='utf-8')
        results = soup.select(".result")
        parse_results = []
        for result in results:
            movie = result.find("h3", class_="product_title").find("a")
            parse_results.append({"url":movie['href'].encode('utf8'), "name": movie.string.encode('utf8')})
        return parse_results

    def parse_html(self, html_cont):
        if html_cont is None or len(html_cont) == 0:
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding='utf-8')
        new_urls = self.parse_new_urls(soup)
        new_datas = self.parse_new_datas(soup)

        return new_urls, new_datas

    def parse_new_urls(self, soup):
        urls = set()
        links = soup.find_all('a', class_='page_num', href=re.compile(r"user-reviews\?page=\d$"))
        for link in links:
            urls.add(link['href'])
        return urls

    def parse_new_datas(self, soup):
        new_datas = []
        # 用户评论区域
        user_reviews = soup.select("li + .user_review")
        for user_review in user_reviews:
            # 名字
            name = user_review.find("div", class_="name")
            # 评分
            score = user_review.find("div", class_="metascore_w")
            # 日期
            date = user_review.find("div", class_="date")
            # 用户发表的完整评论
            user_com = user_review.find("span", class_="blurb_expanded")
            if user_com is None:
                user_com = user_review.find("div", class_="review_body")
            new_datas.append(name.text.strip().encode('utf8')+"\t"
                             +score.text.encode('utf8')+"\t"
                             +re.sub(' |, ', ',', date.text.encode('utf8'))+"\t"
                             +re.sub('[\n\r<br>]', '', user_com.text.encode('utf8')))
        return new_datas