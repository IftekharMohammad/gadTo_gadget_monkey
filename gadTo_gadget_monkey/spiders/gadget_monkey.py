# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider
from gadTo_gadget_monkey.items import GadtoGadgetMonkeyItem

class GadgetMonkeySpider(scrapy.Spider):
    name = 'gadget_monkey'
    allowed_domains = ['gadgetmonkeybd.com']
    start_urls = ['https://www.gadgetmonkeybd.com/product/115765-Xiaomi-wireless-charging-pad-10w-Max']
    
    def parse(self, response):
        item = GadtoGadgetMonkeyItem()
        item['website_name'] = 'Gadget Monkey'
        item['catagory_name'] = 'accessories'
        item['device_name'] = [response.xpath(".//*[@class='row distance single-product-title']/h3/text()").extract_first()]
        item['price'] = [response.xpath(".//*[@class='row distance']/span[@class='price']/text()").extract_first()]
        item['image_urls'] = [response.xpath(".//html/body/div[8]/div[2]").extract_first()]
        item['details'] = [response.xpath('.//*[@id="section-1"]').extract_first()]
        yield item
        next_page = response.xpath(".//*[@class='img-block']/a/@href").extract_first()
        print(next_page)
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)