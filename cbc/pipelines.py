# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import Stories, db_connect, create_stories_table
from models import Comments, create_comments_table


class CbcPipeline(object):
    """CBC stories pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates stories table.
        """
        engine = db_connect()
        create_stories_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save stories in the database.
        This method is called for every item pipeline component.
        """
        if 'cbc_pipe' not in getattr(spider, 'pipelines', []):
            return item

        session = self.Session()
        story = Stories(**item)
        # print "The link is:" + story.link[0]
        try:
            result = (session.execute("select * from stories where link='{" +
                      story.link[0] + "}'"))
            if result.rowcount == 0:
                session.add(story)
                session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item


class CommPipeline(object):
    """CBC comments pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates comments table.
        """
        engine = db_connect()
        create_comments_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save comments in the database.
        This method is called for every item pipeline component.
        """
        if 'comm_pipe' not in getattr(spider, 'pipelines', []):
            return item

        session = self.Session()
        comment = Comments(**item)

        try:
            result = (session.execute("select * from stories where link = '{" +
                      comment.comm_text[0] + "}'"))
            if result.rowcount == 0:
                session.add(comment)
                session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
