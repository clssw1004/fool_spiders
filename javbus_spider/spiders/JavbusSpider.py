import scrapy
from scrapy.selector import Selector


from scrapy.spider import CrawlSpider


class JavbusSpider(CrawlSpider):
    name = 'javbus'
    allow_domains = ['javbus.com']

    def start_requests(self):
        urls = [
            'https://www.javbus.com',
            'https://www.javbus.com/uncensored'
        ]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        sel = Selector(response)
        print(response.body)
        avs = sel.xpath('//div[@id="waterfall"]//div[@class="item"]')
        for av in avs:
            print(av)
