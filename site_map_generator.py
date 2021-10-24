import csv
import sys
import logging
from threading import Thread

from pysitemap import crawler
import time
from database import SiteName, SiteUrl, created
from files import file
result = []


class Maps(Thread):

    def __init__(self, url_map):
        super().__init__()
        self.url_map = url_map
        self.count = 0
        self.file = self.url_map.split('/')
        self.name = self.file[2] + '.xml'
        self.get_time = []

    def get_sitemap(self):
        """get urls"""
        if '--iocp' in sys.argv:
            from asyncio import events, windows_events
            sys.argv.remove('--iocp')
            logging.info('using iocp')
            el = windows_events.ProactorEventLoop()
            events.set_event_loop(el)
        start_time = time.time()
        crawler(str(self.url_map), out_file=f'{self.file[2]}.xml', exclude_urls=[".pdf", ".jpg", ".zip"])
        end_time = time.time()
        times = round(start_time - end_time, 6)
        self.get_time.append(times)
        return 'Ok'

    def get_count(self):
        """Save db, get count url"""
        sitemap = SiteName(name=self.file[2])
        sitemap.save()
        with open(self.name, 'r', encoding='utf-8') as ff:
            for url_file in ff:
                siteurls = SiteUrl(url_names=self.file[2], urls=url_file)
                siteurls.save()
                self.count += 1

    def run(self):
        """run app"""
        self.get_sitemap()
        self.get_count()
        result.append((self.url_map, self.get_time, self.count, self.name))


if __name__ == '__main__':
    db = created
    """add your urls"""
    urls = ['http://crawler-test.com/', 'http://google.com/', 'https://vk.com', 'https://yandex.ru',
            'https://stackoverflow.com']
    tred = [Maps(url).run() for url in urls]
    file(result)


