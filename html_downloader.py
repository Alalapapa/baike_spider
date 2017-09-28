# -*- coding:utf-8 -*-

import urllib2

class HtmlDownload(object):
    def download(self, newUrl):
        if newUrl is None:
            return None
        read = "null"
        try:
            response = urllib2.urlopen(newUrl)
            code = response.getcode()
            read = response.read()
            if code != 200:
                return None
        except Exception as err:
            print err.__str__()
        return read
