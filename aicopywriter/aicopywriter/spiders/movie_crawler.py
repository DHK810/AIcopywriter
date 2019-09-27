# -*- coding: utf-8 -*-
import re
import scrapy
from aicopywriter.items import AicopywriterItem
from datetime import timedelta, date
from urllib import parse
import time
import random
from time import sleep

url_format = 'https://www.imdb.com/search/title/?genres={}&title_type=movie'

genres = ['comedy', 'sci-fi', 'horror', 'romance', 'action', 'thriller',
         'drama', 'mystery', 'crime', 'animation', 'adventure', 'fantasy',
         'comedy-romance', 'action-comedy', 'superhero']


base_url = "www.imdb.com"

class movie_crawlerSpider(scrapy.Spider):
    
    name = 'movie_crawler'
    allowed_domains = ['imdb.com']
    start_urls = []
    
    for genre in genres:    
        start_urls.append(url_format.format(genre))

    def start_requests(self):
        #https://www.imdb.com/feature/genre?ref_=fn_asr_ge
        for u in self.start_urls:
            yield scrapy.Request(u, self.parse_url)

    def parse_url(self, response):
        for movie_list in response.xpath("//h3[@class='lister-item-header']/a/@href").extract():
            url = movie_list
            
            yield response.follow(url, self.parse_details)
        
        #next page
        if response.xpath("//div[@class='desc']/a[@class='lister-page-next next-page']/@href").get() is not None:
        
            next_page = response.xpath("//div[@class='desc']/a[@class='lister-page-next next-page']/@href").get()                
            yield response.follow(next_page, callback = self.parse_url)



    def parse_details(self, response):
        
        item = AicopywriterItem()
        item['movie_name'] = response.xpath("//div[@class='title_wrapper']/h1/text()").get()
        movie_genre = response.xpath("//div[@class='see-more inline canwrap']/a/text()").extract()
        item['movie_genre'] = ' '.join(movie_genre).split()
        if response.xpath("//div[@class='slate_wrapper']/div/a/@href").get() is not None:
            item['movie_poster'] = base_url + response.xpath("//div[@class='slate_wrapper']/div/a/@href").get()
        elif response.xpath("//div[@class='poster']/a/@href").get() is not None:
            item['movie_poster'] = base_url + response.xpath("//div[@class='poster']/a/@href").get()
        else:
            pass

        #tagline이 여러개 인 경우 see more 버튼을 눌러서 새로운 링크로 들어가야함    
        if response.xpath("//div[@class='article']/div[@class = 'txt-block']/text()").get() is not None:
            tagline = response.xpath("//div[@id='titleStoryLine']/div[3]/text()").extract()
            item['movie_tagline'] = re.sub(' {2,}|\\{1,}\n', '', str(tagline))
        else:
            pass

        #summary가 없는 경우 item return
        if 'Add' in response.xpath("//div[@class='article']/span[@class='see-more inline']/a/text()").get():
            yield item
        else:
            summary_url = response.xpath("//div[@class='article']/span[@class='see-more inline']/a/@href").get()
            request = scrapy.Request(response.urljoin(summary_url), callback = self.parse_summary)
            request.meta['item'] = item
            yield request
    
    def parse_summary(self, response):
        
        item = response.request.meta['item']

        if response.xpath("//ul[@id = 'plot-summaries-content']/li[@class='ipl-zebra-list__item']/p/text()").extract() is not None:
            item['movie_summary'] = response.xpath("//ul[@id = 'plot-summaries-content']/li[@class='ipl-zebra-list__item']/p/text()").extract()

            if response.xpath("//ul[@id = 'plot-synopsis-content']/li[@class='ipl-zebra-list__item']/text()").extract() is not None:
                item['movie_synopsis'] = response.xpath("//ul[@id = 'plot-synopsis-content']/li[@class='ipl-zebra-list__item']/text()").extract()
                yield item
            else:

                yield item

            
        
        

            