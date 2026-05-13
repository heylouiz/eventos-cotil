import scrapy


class EventoItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    date_start = scrapy.Field()
    date_end = scrapy.Field()
    time_start = scrapy.Field()
    time_end = scrapy.Field()
    categories = scrapy.Field()
    page = scrapy.Field()
