# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class JdPipeline(object):
    def open_spider(self, spider):
        path = os.path.join(os.getcwd(), 'data', '{}.txt'.format(spider.name))
        self.fa = open(path, 'a+')

    def close_spider(self, spider):
        self.fa.close()

    def process_item(self, item, spider):
        self.fa.write('{}\n'.format(str(item['info'])))
