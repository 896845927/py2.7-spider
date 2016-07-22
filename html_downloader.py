#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import requests

class HtmlDownloader(object):

    def download_html(self, new_url):
        if new_url is None:
            return None
        headers = {'user-agent': 'Chrome/51.0.2704.103'}
        r = requests.get(new_url, headers=headers)
        r.raise_for_status()
        return r.text.encode('utf-8')