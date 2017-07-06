# -*- coding: utf-8 -*-
import scrapy


class ImdbtopSpider(scrapy.Spider):
    name = 'imdbtop'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/chart/top']

    def parse(self, response):
        i=0
        totalrating = 0.0
        for movie in response.css('tr')[1:-2]:
        	r = float(movie.css('td.ratingColumn.imdbRating strong::text').extract_first())
        	totalrating += r
        	yield{
        	'rank': movie.css('td.titleColumn::text').re('[0-9]+')[0],
        	'title': movie.css('td.titleColumn a::text').extract_first(),
        	'link': "http://imdb.com"+str(movie.css('td.titleColumn a::attr(href)').re("(.*)[?]")[0]),
        	'year': movie.css('td span::text').extract_first(),
        	'rating': r
        	}
        	i+=1
        if(i > 0):
        		yield {"average rating": totalrating/i}