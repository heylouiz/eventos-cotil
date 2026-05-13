class EventSummary:
    def __init__(self, element):
        self._el = element

    @property
    def title(self):
        return self._el.css(".rtin-right h3 a::text").get("").strip()

    @property
    def url(self):
        return self._el.css(".rtin-right h3 a::attr(href)").get()

    @property
    def date_label(self):
        day = self._el.css(".rtin-calender h3::text").get("").strip()
        month = self._el.css(".rtin-calender p::text").get("").strip()
        year = self._el.css(".rtin-calender span::text").get("").strip()
        return f"{day} de {month} de {year}"

    @property
    def time_text(self):
        return self._el.css("li.rtin-time::text").get("").strip()


class ListingPage:
    def __init__(self, response):
        self._response = response

    @property
    def events(self):
        return [
            EventSummary(el)
            for el in self._response.css("div.rtin-item")
            if el.css(".rtin-right h3 a::attr(href)").get()
        ]

    @property
    def next_page_url(self):
        return self._response.css(
            ".pagination-area li.active + li a::attr(href)"
        ).get()
