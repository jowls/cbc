--== Web scraping the CBC on Raspberry Pi ==--

Dependencies:

psycopg2
scrapy
sqlalchemy

Special Requirements:

Edit this file after installing selenium:

sudo nano /usr/local/lib/python2.7/dist-packages/selenium/webdriver/firefox/firefox_binary.py

and on line 91 in the wait_until_connectable function change count == 30 to count == 80 in order to allow for the pi's specs.

Instructions:

"scrapy crawl cbc" will run manually

or put this in /etc/crontab to schedule crawl:

17 * * * * pi /home/pi/cbc/crawl.sh >> /home/pi/cronwork.log 2>&1
37 * * * * root sudo killall crawl.sh
38 * * * * root sudo killall Xvfb
39 * * * * root sudo killall iceweasel

(The above runs at 17m past the hour - on raspbian wheezy)
