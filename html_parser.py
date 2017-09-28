# -*- coding:utf-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self, newUrl, htmlCont):
        if newUrl is None or htmlCont is None:
            return
        soup = BeautifulSoup(htmlCont,'html.parser',from_encoding='utf-8')
        newUrls = self._getNewUrls(newUrl,soup)
        newData = self._getNewData(newUrl,soup)
        return newUrls,newData

    def _getNewUrls(self, newUrl, soup):
        newUrls = set()
        # /item/****
        links = soup.find_all('a',href=re.compile(r"/item/"))
        for link in links:
            newLink = link['href']
            newFullLink = urlparse.urljoin(newUrl,newLink)
            newUrls.add(newFullLink)
        return newUrls

    def _getNewData(self, newUrl, soup):
        resData = {}

        # url
        resData['url'] = newUrl

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find("h1")
        resData['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_="lemma-summary")
        resData['summary'] = summary_node.get_text()

        return resData
