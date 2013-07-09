# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
import time
from cbc.items import CommentItem
from selenium import webdriver
from sqlalchemy.orm import sessionmaker
from cbc.models import db_connect, Stories
from pyvirtualdisplay import Display
import datetime

class CommSpider(BaseSpider):
    name = "comm"
    engine = db_connect()
    sm = sessionmaker(bind=engine)
    session = sm()
    result = (session.execute("select * from stories where crawled_on is null and comments_open is not False"))  # lint:ok
    abort = False
    try:
        start_url_brackets = result.first()['link']
        print start_url_brackets
        start_url = start_url_brackets[1:-1]
        #start_urls = ["http://www.cbc.ca/news/canada/new-brunswick/story/2013/06/14/nb-alcohol-testing-irving-supreme.html"]
        print start_url
        start_urls = [start_url]
        #start_urls = ["http://www.cbc.ca/news/canada/new-brunswick/story/2013/06/16/nb-car-crash.html"]
    except:
        abort = True
    pipelines = ['comm_pipe']

    #def __init__(self):
        #time.sleep(60)

        #time.sleep(60)
    #def __del__(self):
        #self.selenium.stop()
        #print self.verificationErrors
     #   BaseSpider.__del__(self)

    def parse(self, response):
        items = []
        if self.abort == True:
            return items
        display = Display(visible=0, size=(800, 600))
        display.start()
        fp = webdriver.FirefoxProfile()
        fp.set_preference("dom.max_script_run_time", 0)
        fp.set_preference("dom.max_chrome_script_run_time", 0)
        path = "/home/pi/cbc/adblockedge-2.0.4.xpi"
        fp.set_preference("extensions.adblockedge.currentVersion", "2.0.4")
        fp.add_extension(extension=path)
        self.driver = webdriver.Firefox(firefox_profile=fp)
        #print("Inside parse. Waiting 45 seconds now.")
        #time.sleep(45)
        #print("After sleep now.")
        self.driver.get(response.url)
        print("Got response now.")
        engine = db_connect()
        sm = sessionmaker(bind=engine)
        session = sm()
        time.sleep(5)
        try:
            self.driver.find_element_by_link_text("submission guidelines")
        except:
            #print "exception"
            link = session.query(Stories).filter_by(link=self.start_url_brackets).first()
            link.comments_open = False
            session.commit()
            return items
        while True:
            #comm = self.driver.find_element_by_xpath("//div[contains(@class,'vf-horizontal-list')]")
            comm = self.driver.find_element_by_class_name("vf-horizontal-list")
            comments = comm.find_elements_by_class_name("vf-comment-thread")
            time.sleep(8)
            st = (session.execute("select * from stories where link like '%" + self.start_url + "%'"))  # lint:ok
            st_id = st.first()['id']
            for comment in comments:
                item = CommentItem()
                tmp_a = comment.find_element_by_xpath(".//p[contains(@class, 'vf-comment-html')]")
                item['comm_text'] = tmp_a.text
                tmp_b = comment.find_element_by_xpath(".//span[contains(@class, 'vf-username')]")
                item['user_name'] = tmp_b.text
                item['story_id'] = st_id
                items.append(item)
            try:
                self.driver.find_element_by_link_text("Show More").click()
            except:
                break
        link = session.query(Stories).filter_by(link=self.start_url_brackets).first()
        link.crawled_on = datetime.datetime.now()
        session.commit()
        self.driver.close()
        display.stop()
        return items
