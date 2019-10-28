#!/usr/bin/env python3

import requests
from lxml import html
import os

mainUrl = "**************"
last_url_number: int
count = 0
local_path = r'******\NewsScraping'
txt_path = local_path + r"\Scraper" + r"\url_number.txt"
path = local_path + r'\File'
with open(txt_path, "r") as f:
    last_url_number = int(f.read().split(",")[-1])
while count < 10:
    url = mainUrl + "/info/" + str(last_url_number) + ".jspx"

    page = requests.Session().get(url)

    if page:
        tree = html.fromstring(page.content)
        div = tree.xpath(u'//div[@class = "art"]')
        h1 = tree.xpath(u'//div[@class = "art"]/h1')
        time = tree.xpath(u'//div[@class = "art_time"]//li/text()')
        p = tree.xpath(u'//div[@class = "art"]/p//text()')
        a = tree.xpath(u'//div[@class = "art"]/p/span/a/@href')
        a_text = tree.xpath(u'//div[@class = "art"]/p/span/a/text()')

        os.mkdir(path + './%s' % str(last_url_number))
        # print(div[0])
        # print(h1[0].text)
        # print(time[0])
        file_name = './%d' % last_url_number + './' + h1[0].text + time[0] + '.txt'

        if p:
            # for i in range(len(p)):
            #     print(p[i])
            f = open(path + file_name, 'a', encoding='utf-8')
            for i in range(len(p)):
                f.write(p[i])
            f.close()

        if a:
            for i in range(len(a)):
                # print(mainUrl + a[i])
                # print(a_text[i])
                file = path + './%d' % last_url_number + './%s' % a_text[i]
                r = requests.get(mainUrl + a[i])
                with open(file, "wb") as f:
                    f.write(r.content)
                f.close()

        with open(txt_path, 'a+') as f:
            f.write("," + str(last_url_number + 1))

        break

    else:
        count = count + 1
        last_url_number = last_url_number + 1


