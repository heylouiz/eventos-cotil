class EventPage:
    def __init__(self, response):
        self._response = response
        self._info = self._parse_info()

    def _parse_info(self):
        info = {}
        for li in self._response.css(".event-info ul li"):
            label = li.css("span::text").get("").strip().rstrip(":")
            value = "".join(li.xpath("./text()").getall()).strip()
            if label and value:
                info[label] = value
        return info

    @property
    def title(self):
        return self._response.css("h1.entry-title::text").get("").strip()

    @property
    def categories(self):
        return self._response.css(
            "a.taxonomy.ac_event_category span::text"
        ).getall()

    @property
    def date_start(self):
        return self._info.get("Data de Início", "")

    @property
    def time_start(self):
        return self._info.get("Horário de Início", "")

    @property
    def date_end(self):
        return self._info.get("Data de Fim", "")

    @property
    def time_end(self):
        return self._info.get("Horário de Fim", "")
