# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GadtoGadgetMonkeyItem(scrapy.Item):
	website_name = scrapy.Field()
	catagory_name = scrapy.Field()
	device_name = scrapy.Field()
	price = scrapy.Field()
	image_urls = scrapy.Field()
	details = scrapy.Field()
