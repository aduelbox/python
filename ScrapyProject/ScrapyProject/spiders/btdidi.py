# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import get_base_url
from urllib import parse
from scrapy.http import Request
import re
from ScrapyProject.items import BtdidiItem


class BtdidiSpider(scrapy.Spider):
    name = 'btdidi'
    allowed_domains = ['www.btwhat.info']
    start_urls = ['http://www.btwhat.info/search/b-5L%2bu5q2j.html']


    def parse(self, response):
        """
            1. 获取列表页中的搜索结果url并交给scrapy下载后并进行解析
            2. 获取下一页的url并交给scrapy进行下载，下载完成后交给parse
        """

        # 解析列表页中的所有搜索结果url并交给scrapy下载后并进行解析
        search_item = response.css("#wall .search-item")
        for item in search_item:
            size_str = item.css(".item-bar .yellow-pill::text").extract_first()
            if size_str:
                # size_re = re.match("^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$", size_str).group()
                size_re = re.match("^([1-9]\d*(\.\d*[1-9])?)|(0\.\d*[1-9])$", size_str).group()
                size_float = float(size_re)
                if size_float >= min_size:
                    url = item.css(".item-title h3 a::attr(href)").extract_first()
                    print("文件大小：", size_str, "链接：", parse.urljoin(response.url, url))
                    yield Request(url=parse.urljoin(response.url, url), callback=self.parse_detail)
            # size = response.css("#wall .item-bar .yellow-pill").extract()
            # urls = response.css("#wall .search-item .item-title h3 a::attr(href)").extract()
            # for url in urls:
            #     print(parse.urljoin(response.url, url))
            #     yield Request(url=parse.urljoin(response.url, url), callback=self.parse_detail)

        # 提取下一页并交给scrapy进行下载
        next_url = response.css(".bottom-pager a::attr(href)").extract()[-1]

        if next_url:
            print(parse.urljoin(response.url, next_url))
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        # 解析磁链地址
        title = response.xpath("//meta[@name='keywords']")
        magnet_path = response.css(".fileDetail>div>.panel-body>a::attr(href)").extract_first()
        print("磁链地址：", magnet_path)

        magnet_item = BtdidiItem()
        magnet_item['magnet'] = magnet_path
        yield magnet_item
