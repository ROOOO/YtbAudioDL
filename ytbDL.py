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
    self.files = []
    self.audioPostfix = ['aac', 'vorbis', 'mp3', 'm4a', 'opus', 'wav', 'ogg']

  def getHTML(self, url):
    self.address = 'http://' + url + self.address
    print u'opening ' + self.address
    request = urllib2.Request(self.address)
    self.html = urllib2.urlopen(self.address).read()

  def searchLocalExistsAudioFiles(self):
    fileNames = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    for fileName in fileNames:
      if os.path.splitext(fileName)[1] + '.' in self.audioPostfix:
        self.files.append(fileName)

  def getAudioFiles(self):
    pattern = re.compile(r'<li><a href="(.*?)">(.*?)</a>')
    items = re.findall(pattern, self.html)
    for item in items:
      if re.search(re.compile(r'\.'), item[1]) and re.split(re.compile(r'\.'), item[1])[1] in self.audioPostfix and item[1] not in self.files:
        os.popen('wget ' + self.address + '/' + item[0])

if __name__ == '__main__':
  opts, args = getopt.getopt(sys.argv[1:], 'p:')
  if len(args) > 1 or args == []:
    print u'Usage: python ytbmp3Local.py [OPTIONS] IP'
  else:
    YTB = YtbMP3Local(opts)
    YTB.getHTML(args[0])
    YTB.searchLocalExistsAudioFiles()
    YTB.getAudioFiles()
