# coding: utf-8
import re
import urllib
import urllib2
from bs4 import BeautifulSoup
import sys

__author__ = 'Muneyuki Kitano'

class Crawler4U:
    """
    Crawler4U is the crawler to get the image of the idol from 4U.
    """

    def __init__(self, word, path):
        self.word = word
        self.path = path

    def crawl(self):
        """
        Extract URL of detail page from list.
        """
        base_url = "http://4u-beautyimg.com/list.php"
        page = 0
        while True:
            url = base_url + "?name=" + urllib.quote(word.decode("shift-jis").encode("utf-8")) + "&lim=" + str(page)
            print url
            f = urllib2.urlopen(url)

            res = BeautifulSoup(f.read())

            if res.find(href=re.compile("image/")) is None:
                sys.exit()

            for link in res.find_all(href=re.compile("image/")):
                detail_url = "http://4u-beautyimg.com/" + link.get("href")
                self._find_image(detail_url)
            page += 13

    def _find_image(self, detail_url):
        """
        Find URL of image from detail page.
        """
        detail_page = urllib2.urlopen(detail_url)
        soup = BeautifulSoup(detail_page.read())

        file = open(path, "a")
        file.write(detail_url)
        file.write(",")

        for img in soup.find_all("img"):
            if img.get("alt") == word.decode("shift-jis"):
                file.write(img.get("src"))
                file.write(",")

        if len(soup.select("td.t-left a")) == 0:
            file.write("none.")
            file.write("\n")
        else:
            origin = str(soup.select("td.t-left a")[0].get("href"))
            file.write(origin)
            file.write("\n")
        file.close()

# Execute
word = sys.argv[1]  # example: "吉木りさ"
path = sys.argv[2]  # example: "c:\\4uBeauty\\list.csv"

crawler = Crawler4U(word, path)
crawler.crawl()
