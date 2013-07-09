# Scrapy settings for cbc project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'cbc'
VERSION = '1.0'

SPIDER_MODULES = ['cbc.spiders']
NEWSPIDER_MODULE = 'cbc.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, VERSION)

DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': '~~~REMOVED~~~',
            'password': '~~~REMOVED~~~',
            'database': '~~~REMOVED~~~'}

ITEM_PIPELINES = ['cbc.pipelines.CbcPipeline', 'cbc.pipelines.CommPipeline']
