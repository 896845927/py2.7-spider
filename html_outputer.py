#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import time


class HtmlOutputer(object):
    def __init__(self):
        self.data = []

    def collect_data(self, new_data):
        self.data.extend(new_data)

    def output(self, movie_name):
        file_name = time.strftime("%Y-%m-%d", time.localtime())+"-metacritic-"+movie_name+".txt"
        with open(file_name, "w") as f:
            f.writelines(self.data)
