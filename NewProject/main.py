import os.path
import random
import time

import requests
import lxml.etree

page_n = int(input("请输入你想要爬取的网站数量"))

for i in range(page_n):
    url = f'https://www.tuke88.com/yinxiao/zonghe_0_{i}.html'
    response = requests.get(url)
    # 这一步只返回了 200
    html_parser = lxml.etree.HTMLParser()
    html = lxml.etree.fromstring(response.text, parser=html_parser)
    titles = html.xpath("//div[@class='lmt']//div[@class='aduio-list']//a[@class='tittle']/text()")
    mp3_urls = html.xpath("//div[@class='lmt']//div[@class='aduio-list']//source/@src")

    if not os.path.exists('pymp3'):
        os.mkdir('pymp3')
    for title, mp3_url in zip(titles, mp3_urls):
        mp3_stram = requests.get(mp3_url, stream=True)
        with open(os.path.join('pymp3', title + ".mp3"), 'wb+') as writer:
            writer.write(mp3_stram.raw.read())
            print(f'[Info]{title}.mp3下载成功')
            time.sleep(random.uniform(0.1, 0.4))
