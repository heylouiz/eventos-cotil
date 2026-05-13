import scrapy
from eventos_cotil.items import EventoItem


class CotilSpider(scrapy.Spider):
    name = "cotil"
    allowed_domains = ["cotil.unicamp.br"]
    start_urls = ["https://www.cotil.unicamp.br/eventos"]

    def __init__(self, max_pages=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_pages = int(max_pages) if max_pages is not None else None

    def parse(self, response):
        page = response.meta.get("page", 1)

        for item in response.css("div.rtin-item"):
            day = item.css(".rtin-calender h3::text").get("").strip()
            month = item.css(".rtin-calender p::text").get("").strip()
            year = item.css(".rtin-calender span::text").get("").strip()
            time_text = item.css("li.rtin-time::text").get("").strip()
            url = item.css(".rtin-right h3 a::attr(href)").get()
            title = item.css(".rtin-right h3 a::text").get("").strip()

            if url:
                meta = {
                    "title": title,
                    "date_label": f"{day} de {month} de {year}",
                    "time_text": time_text,
                    "page": page,
                }
                yield response.follow(url, self.parse_event, meta=meta)

        if self.max_pages is not None and page >= self.max_pages:
            return

        next_page = response.css(".pagination-area li.active + li a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse, meta={"page": page + 1})

    def parse_event(self, response):
        item = EventoItem()
        item["url"] = response.url
        item["title"] = response.css("h1.entry-title::text").get(
            response.meta["title"]
        ).strip()
        item["categories"] = response.css(
            "a.taxonomy.ac_event_category span::text"
        ).getall()

        info = {}
        for li in response.css(".event-info ul li"):
            label = li.css("span::text").get("").strip().rstrip(":")
            value = "".join(li.xpath("./text()").getall()).strip()
            if label and value:
                info[label] = value

        item["date_start"] = info.get("Data de Início", response.meta["date_label"])
        item["time_start"] = info.get("Horário de Início", "")
        item["date_end"] = info.get("Data de Fim", "")
        item["time_end"] = info.get("Horário de Fim", "")
        item["page"] = response.meta["page"]

        yield item
