## What is Scrapy?
Scrapy is a free and open-source web-crawling framework written in python.

It was originally designed for web scrapping but can also be used for extracting the data using the APIs or as a general purpose web crawler.

It is currently maintained by Scrapinghub Ltd.

## What is A WebCrawler?
A web-crawler is also known as a web spider, automatic indexer or simply crawler.

It is an internet bot that helps in web indexing

Web crawlers helps in collecting information from a webpage and the links related to them

It also helps in validating HTML code and hyperlinks.

They crawl one page at a time until all the pages are indexed.

## How to Install Scrapy?
To install scrapy, simply run the following in the command prompt or in the terminal, or simply you can add the package from the project interpreter too.

        pip install scrapy

## Create a project

    syntax :- scrapy startproject project_name
    
    Ex :- scrapy startproject dineout

## Run the Project

    scrapy crawl dineout_spider -a state=delhi -O data/dineout.json


## Reference

[Scrapy documentation link](https://docs.scrapy.org/en/latest/index.html)