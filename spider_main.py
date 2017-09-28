# -*- coding:utf-8 -*-

# 爬虫总调main函数
from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        # 初始化url管理器
        self.urls = url_manager.UrlManager()
        # 初始化下载器
        self.downloader = html_downloader.HtmlDownload()
        # 初始化解析器
        self.parser = html_parser.HtmlParser()
        # 初始化输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        # 计数
        count = 1
        self.urls.addNewUrl(root_url)
        while self.urls.hasNewUrl():
            try:
                newUrl = self.urls.getNewUrl()
                print 'craw %d : %s'%(count,newUrl)
                htmlCont = self.downloader.download(newUrl)
                newUrls,newData = self.parser.parse(newUrl,htmlCont)
                self.urls.addNewUrls(newUrls)
                self.outputer.collectData(newData)
                if count == 50:
                    break
                count = count+1
            except:
                'craw failed'
        self.outputer.outputHtml()


if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
