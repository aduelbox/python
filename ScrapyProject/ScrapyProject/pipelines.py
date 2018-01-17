# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyprojectPipeline(object):
    def process_item(self, item, spider):
        return item


class MagnetPipeline(object):
    def process_item(self, item, spider):
        print(item['magnet'])
        file = open("修正.txt", "a")
        file.writelines(item['magnet'] + "\n")
        file.close()
        return item
