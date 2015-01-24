# coding: utf-8
import csv
import os
import urllib2
import sys

__author__ = 'Muneyuki Kitano'

class CsvDownLoader:

    def __init__(self, list, path):
        self.list = list
        self.path = path

    def _dl_image(self, param):
        try:
            filename = os.path.basename(param)
            if not os.path.exists(path + filename):
                req = urllib2.Request(param)
                req.add_headers = [('User-agent', 'Mozilla/5.0')]
                image = urllib2.urlopen(req).read()
                local_file = open(path + filename, "wb")
                local_file.write(image)
                local_file.close()
        except Exception, e:
            print e

    def dl(self, col):
        with open(list, "rb") as f:
            reader = csv.reader(f)
            for row in reader:
                print row[col]
                self._dl_image(row[col])

if __name__ == '__main__':
    list = sys.argv[1]  # "c:\\list.csv"
    path = sys.argv[2]  # output directory
    col = 1  # csv column
    downloader = CsvDownLoader(list, path)
    downloader.dl(col)
