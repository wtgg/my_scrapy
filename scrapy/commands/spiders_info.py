from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):

    requires_project = True
    default_settings = {'LOG_ENABLED': False}

    def short_desc(self):
        return "List atrrs of spiders"

    def run(self, args, opts):
        import json
        spiders = self.crawler_process.spider_loader.spiders()
        spiders_str = json.dumps(spiders, ensure_ascii=False)
        print(spiders_str)
        # print(type(spiders))
        # print(type(spiders_str))
        # for spider in self.crawler_process.spider_loader.spiders():
        #     print(spider)
