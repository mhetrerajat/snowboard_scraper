import logging
import os

from scrapy.dupefilters import RFPDupeFilter
from scrapy.utils.request import request_fingerprint


class CookieDuplicateFilter(RFPDupeFilter):
    """
        A dupe filter that considers combination of url and site_country_id cookie
    """

    def __getid(self, url, site_country_id):
        return "{0}?site_country_id={1}".format(url, site_country_id)

    def request_seen(self, request):
        fp = self.__getid(request.url, request.cookies.get('site_country_id'))
        if fp in self.fingerprints:
            return True
        self.fingerprints.add(fp)
        if self.file:
            self.file.write(fp + os.linesep)
