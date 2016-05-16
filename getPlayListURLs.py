# coding: utf-8

__author__ = 'King'

import re
import urllib
import urllib2
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import platform

class getPlayListURLs:
  def __init__(self, url):
    self.playlistURL = url
    self.urls = []
    self.names = []

    sysstr = platform.system()
    if sysstr == 'Linux':
      self.driver = webdriver.PhantomJS(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'phantomjs'))
    elif sysstr == 'Windows':
      # self.driver = webdriver.PhantomJS('./phantomjs_win.exe')
      self.driver = webdriver.Chrome()
    self.wait = WebDriverWait(self.driver, 30)

  def getURLs(self):
    self.driver.get(self.playlistURL)
    pattern = re.compile(r'a class.*?title="(.*?)".*?href="(.*?)"', re.S)
    pageHTML = self.driver.page_source
    # print pageHTML
    items = re.findall(pattern, pageHTML)
    for item in items:
      if re.match(r'\Wplaylist', item[1]):
        self.names.append(item[0])
        self.urls.append(item[1])
    self.driver.quit()
    self.ask()

  def ask(self):
    input1 = ''
    while input1 != 'GO':
      num = 0
      for item in self.names:
        num += 1
        print str(num) + '. ' + item
      count = len(self.names)
      input1 = raw_input('Which one you do not want to download?(input GO for continue)')
      if input1 == 'GO':
        break
      try:
        input1 = int(input1)
      except:
        pass
      else:
        if input1 > 1 and input1 <= count:
          self.names.remove(self.names[input1 - 1])
          self.urls.remove(self.urls[input1 - 1])

    self.save()

  def save(self):
    file = open('toBeDownload', 'w')
    for item in self.urls:
      file.write('https://www.youtube.com' + item + '\n')
    file.close()

if __name__ == '__main__':
  prefix = u'https://'
  html = sys.argv[1]
  pattern = re.compile(prefix)
  if not re.match(pattern, html):
    html = prefix + html

  getURL = getPlayListURLs(html)
  getURL.getURLs()
  # if :
  #   print u'Usage: python ytbmp3Local.py [OPTIONS] IP'
  # else:
  #   YTB = YtbMP3Local(opts)
  #   YTB.getHTML(args[0])
  #   YTB.searchLocalExistsAudioFiles()
  #   YTB.getAudioFiles()
