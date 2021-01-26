from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):

    requires_project = True
    default_settings = {'LOG_ENABLED': False}

    def short_desc(self):
        return "List available spiders"

    def run(self, args, opts):
        import json
        attrs = self.crawler_process.spider_loader.attrs()
        attrs_str = json.dumps(attrs, ensure_ascii=False)
        print(attrs_str)
        # for s in sorted(self.crawler_process.spider_loader.attrs()):
        #     print(s)
