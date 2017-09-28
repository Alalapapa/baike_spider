# -*- coding:utf-8 -*-

class UrlManager(object):

    def __init__(self):
        self.newUrls = set()
        self.oldUrls = set()

    # 向UrlManager添加一个url
    def addNewUrl(self, url):
        if url is None:
            return
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)


    # 向UrlManager添加一组url
    def addNewUrls(self, newUrls):
        if newUrls is None or len(newUrls) == 0:
            return
        for url in newUrls:
            self.addNewUrl(url)

    # 判断UrlManager中是否还有新的待爬取url
    def hasNewUrl(self):
        return len(self.newUrls) != 0

    # 从UrlManager获取一个新的待爬取url
    def getNewUrl(self):
        newUrl = self.newUrls.pop()
        self.oldUrls.add(newUrl)
        return newUrl

