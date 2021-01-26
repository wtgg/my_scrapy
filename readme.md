### scrapy 新增命令 `scrapy spiders_info`
### scrapyd 新增接口 get curl http://123.45.67.89:6800/spidersinfo.json?project=youtube
```
scrapy spiders_info 

[{"name": "板块采集", "site_name": "youtube", "spider_type": "板块采集", "t": 1611590400}, {"name": "关键词采集", "site_name": "youtube", "spider_type": "关键词采集", "t": 1611590400}]


```

```
curl http://172.31.49.57:6801/spidersinfo.json?project=youtube
{
    "node_name": "run-spider",
    "status": "ok",
    "spiders_count": 2,
    "spiders_info": [
        {
            "name": "板块采集",
            "site_name": "youtube",
            "spider_type": "板块采集",
            "t": 1611072000
        },
        {
            "name": "关键词采集",
            "site_name": "youtube",
            "spider_type": "关键词采集",
            "t": 1611072000
        }
    ]
}
```