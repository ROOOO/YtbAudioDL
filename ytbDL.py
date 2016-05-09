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
    if opts != []:
      for op, v in opts:
        if op == '-p':
          self.port = v
    self.address = ':' + self.port

  def getHTML(self, url):
    self.address = 'http://' + url + self.address
    print self.address
    request = urllib2.Request(self.address)
    self.html = urllib2.urlopen(self.address).read()

  def getAudioFiles(self):
    pattern = re.compile(r'<li><a href="(.*?)">.*?(aac|vorbis|mp3|m4a|opus|wav|ogg)</a>')
    items = re.findall(pattern, self.html)
    for item in items:
      os.popen('wget ' + self.address + '/' + item[0])

if __name__ == '__main__':
  opts, args = getopt.getopt(sys.argv[1:], 'p:')
  if len(args) > 1 or args == []:
    print u'Usage: python ytbmp3Local.py [OPTIONS] IP'
  else:
    YTB = YtbMP3Local(opts)
    YTB.getHTML(args[0])
    YTB.getAudioFiles()
