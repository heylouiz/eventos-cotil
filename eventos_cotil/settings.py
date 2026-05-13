BOT_NAME = "eventos_cotil"

SPIDER_MODULES = ["eventos_cotil.spiders"]
NEWSPIDER_MODULE = "eventos_cotil.spiders"

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 1

DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
}

FEEDS = {
    "eventos.json": {
        "format": "json",
        "encoding": "utf8",
        "indent": 2,
        "overwrite": True,
    }
}
