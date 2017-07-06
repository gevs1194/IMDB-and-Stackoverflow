# -*- coding: utf-8 -*-
import scrapy


class StackSpider(scrapy.Spider):
    name = 'stack'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/questions/tagged/python?page=1&sort=votes&pagesize=15',
    'http://stackoverflow.com/questions/tagged/python?page=2&sort=votes&pagesize=15',
    'http://stackoverflow.com/questions/tagged/python?page=3&sort=votes&pagesize=15']

    def parse(self, response):
        for stack in response.css('div.summary'):
        	yield {
        	'Question': stack.css('h3 a::text').extract_first(),
        	'Link': stack.css('h3 a::attr(href)').extract_first()
        	}
