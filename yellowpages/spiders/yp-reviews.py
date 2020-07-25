# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import YellowpagesItem


class YwpagesSpider(scrapy.Spider):
    name = 'yp_reviews'
    allowed_domains = ['yellowpages.com']
    start_urls = [
        'https://www.yellowpages.com/dayton-oh/mip/the-original-pancake-house-17684150']

    def parse(self, response):
        sourceURL = response.url
        name = response.css('div.sales-info h1::text').extract_first()
        total_review = response.css(
            'section.ratings span.count').extract_first()
        if total_review != '':
            review_numbers = ''.join(filter(str.isdigit, total_review))
        DivNodes = response.css('div#reviews-container article')
        for divs in DivNodes:
            hash_key = divs.css('::attr(id)').extract_first()
            reviewer_name = divs.css('a.author::text').extract_first()
            if reviewer_name is None:
                reviewer_name = divs.css('div.author::text').extract_first()
            review_date = divs.css(
                'div.review-dates p.date-posted span::text').extract_first()
            reviews = divs.css('div.review-response p::text').extract_first()
            stars_count = divs.css(
                'div.result-ratings div::attr(class)').extract_first()
            if stars_count != '':
                stars_count = stars_count.replace(
                    'rating-indicator', '').strip()
                if stars_count == 'one':
                    rating = '1'
                elif stars_count == 'one half':
                    rating = '1.5'
                elif stars_count == 'two':
                    rating = '2'
                elif stars_count == 'two half':
                    rating = '2.5'
                elif stars_count == 'three':
                    rating = '3'
                elif stars_count == 'three half':
                    rating = '3.5'
                elif stars_count == 'four':
                    rating = '4'
                elif stars_count == 'four half':
                    rating = '4.5'
                else:
                    rating = '5'

            l = ItemLoader(item=YellowpagesItem())

            l.add_value('name', name)
            l.add_value('total_review', review_numbers)
            l.add_value('ratings', rating)
            l.add_value('reviewer_name', reviewer_name)
            l.add_value('reviews', reviews)
            l.add_value('review_date', review_date)
            l.add_value('hash_key', hash_key)
            l.add_value('sourceURL', sourceURL)
            print('\n\n\n', l.load_item())

            yield(l.load_item())
