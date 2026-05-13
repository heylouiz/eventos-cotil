import scrapy
from eventos_cotil.items import EventoItem
from eventos_cotil.pages.listing import ListingPage
from eventos_cotil.pages.event import EventPage


class CotilPOSpider(scrapy.Spider):
    name = "cotil_po"
    allowed_domains = ["cotil.unicamp.br"]
    start_urls = ["https://www.cotil.unicamp.br/eventos"]

    def __init__(self, max_pages=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_pages = int(max_pages) if max_pages is not None else None

    def parse(self, response):
        page_num = response.meta.get("page", 1)
        listing = ListingPage(response)

        for event in listing.events:
            yield response.follow(event.url, self.parse_event, meta={
                "title": event.title,
                "date_label": event.date_label,
                "time_text": event.time_text,
                "page": page_num,
            })

        if self.max_pages is None or page_num < self.max_pages:
            if listing.next_page_url:
                yield response.follow(
                    listing.next_page_url,
                    self.parse,
                    meta={"page": page_num + 1},
                )

    def parse_event(self, response):
        event = EventPage(response)
        item = EventoItem()
        item["url"] = response.url
        item["title"] = event.title or response.meta["title"]
        item["categories"] = event.categories
        item["date_start"] = event.date_start or response.meta["date_label"]
        item["time_start"] = event.time_start
        item["date_end"] = event.date_end
        item["time_end"] = event.time_end
        item["page"] = response.meta["page"]
        yield item
