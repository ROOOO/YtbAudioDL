import urllib2
import getopt
import sys
import re
import os

class YtbMP3Local:
  """docstring for YtbMP3Local"""
  def __init__(self, opts):
    self.html = ''
    self.port = '23333'
    self.output = ''
    if opts != []:
      for op, v in opts:
        if op == '-o':
          self.output = v
    self.address = ':' + self.port + '/'
    self.files = []
    self.prefix = ''

  def getHTML(self, url):
    self.address = url
    prefix = re.findall(r'(.*?)://(.*?)/', url)[0]
    self.prefix = str(prefix[0]) + '://' + str(prefix[1]) + '/'

    print u'opening ' + self.address
    # request = urllib2.Request(self.address)
    self.html = urllib2.urlopen(self.address).read()

  def searchLocalExistsAudioFiles(self):
    fileNames = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    for fileName in fileNames:
      self.files.append(fileName)

  def getAudioFiles(self):
    pattern = re.compile(r'<a href="/(.*?)">(.*?)</a>')
    items = re.findall(pattern, self.html)
    l = len(items)
    c = 0
    for item in items:
      c += 1
      if re.search(re.compile(r'\.'), item[1]) and item[1] != '../' and item[1] not in self.files:
        # os.popen('wget ' + self.address + '/' + item[0])
        if self.output != '':
          os.popen('wget -c ' + '-P ' + self.output + ' ' + self.prefix + item[0])
        else:
          os.popen('wget -c ' + self.prefix + item[0])
        print 'Downloading ' + item[1] + '========' + str(int(c / float(l) * 100)) + u'%'

if __name__ == '__main__':
  opts, args = getopt.getopt(sys.argv[1:], 'o:')
  if len(args) > 1 or args == []:
    print u'Usage: python ytbmp3Local.py [OPTIONS] Address'
  else:
    YTB = YtbMP3Local(opts)
    YTB.getHTML(args[0])
    YTB.searchLocalExistsAudioFiles()
    YTB.getAudioFiles()
