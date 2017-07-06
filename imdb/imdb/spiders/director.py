# -*- coding: utf-8 -*-
import scrapy


class DirectorSpider(scrapy.Spider):
    name = 'director'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/chart/top']

    def parse(self, response):
        if response.url == "http://www.imdb.com/chart/top":
        	tr = response.css('tr')[1:-2]
        	limit = 10
        	if len(tr)<10:
        		limit = len(tr)
        	for movie in range(0,limit): 
        		link = "http://imdb.com"+str(tr[movie].css('td.titleColumn a::attr(href)').re("(.*)[?]")[0])
        		yield scrapy.Request(link)
        else:
        	Movie_title = response.xpath('//title/text()').extract_first()
        	Director_name = response.xpath('//*[@itemprop="director"]/a/span/text()').extract()[0]
        	yield {
        	'Movie title':Movie_title,
        	'Director name':Director_name
        	}