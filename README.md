# Web Scraping with Raspberry Pi

## About

A small project involving web scraping javascript content using: the raspberry pi, python, scrapy and selenium/firefox webdriver. Results are stored in postgresql using the sqlalchemy library. Statistics about the database can optionally be served over the web through a lightweight golang process.

The roadmap is to integrate the nltk library to perform basic sentiment analysis on news articles, and the comments they elicit.

Coming soon.

## Readme Contents

    Setup Pi
    Code
    Configuration
    Golang Webserver (Optional)

## Dependencies:

psycopg2
scrapy
sqlalchemy

## Setup Pi
Install Dependencies

Install raspbian wheezy on a new SD card and boot up Pi.

Install postgresql (9.1.9 at time of writing)
	sudo apt-get install postgresql

Install firefox (iceweasel 10.0.12esr at time of writing) and pip
	sudo apt-get install iceweasel python-pip

Install additional python dependencies using pip (scrapy 16.5, selenium 2.33.0 at time of writing)
	sudo pip install -U scrapy selenium

## Special Requirements

Because of the Pi's limited CPU/GPU, you should make the following adjustment to selenium's firefox webdriver code.
sudo nano /usr/local/lib/python2.7/dist-packages/selenium/webdriver/firefox/firefox_binary.py

on line 91 in the wait_until_connectable function, change count == 30 to be
count == 80

in order to give firefox some extra time to warm up.

## Code

Clone the repository from GitHub
git clone https://github.com/jowls/abcd.git

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
	Testing 1-2-3...

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum

## Cron Job Configuration:

"scrapy crawl cbc" will run the spider manually, or put this in /etc/crontab to schedule some crawls:

	17 * * * * pi /home/pi/cbc/crawl.sh >> /home/pi/cronwork.log 2>&1
	37 * * * * root sudo killall crawl.sh
	38 * * * * root sudo killall Xvfb
	39 * * * * root sudo killall iceweasel

(The above runs at 17m past the hour - on raspbian wheezy)

## Golang Webserver (Optional)

Install go

Build go code
	go build web.go

Run go code

It must be run as sudo because it will be serving on port 80.

	sudo ./web&
