# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class LinkItem(Item):
    title = Field()
    link = Field()
    #descr = Field()
    comments_open = Field()
    crawled_on = Field()


class CommentItem(Item):
    comm_text = Field()
    story_id = Field()
    #t_up = Field()
    #t_down = Field()
    user_name = Field()
    #user_link = Field()
