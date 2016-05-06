import os
import re
import sys, getopt

class YtbMP3Server:
    """docstring for YtbMP3Server"""
    def __init__(self):
        self.addresses = ''
        self.proxy = ''
        self.path = os.path.dirname(os.path.realpath(__file__))

    def download(self, opts, args):
        for address in args:
            self.addresses += (' ' + address)

        for op, v in opts:
            if op == '-p':
                self.proxy = v

        if self.proxy == '':
            dl = os.popen('youtube-dl --audio-quality 0 ' + self.addresses).read()
        else:
            dl = os.popen('youtube-dl --audio-quality 0 --proxy ' + self.proxy + self.addresses).read()

        downloadedFiles = []
        # for dirPath, dirNames, fileNames in os.walk(os.path.dirname(os.path.realpath(__file__))):
        fileNames = os.listdir(self.path)
        for fileName in fileNames:
            if os.path.splitext(fileName)[1] == '.mp4' or os.path.splitext(fileName)[1] == '.mkv':
                downloadedFiles.append(fileName)

        l = float(len(downloadedFiles))
        if int(l) == 0:
            return

        c = 0
        for file in downloadedFiles:
            os.popen('rm ' + '"' + file + '"')
            c += 1
            print str(c / l * 100) + '%   ' + '(' + str(c) + '/' + str(int(l)) + ')'

        self.HTTPServer()

    def HTTPServer():
        try:
            os.popen('python -m SimpleHTTPServer 8080 &')
        except:
            pass

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'p:')
    if len(sys.argv) < 2:
        print u'Usage: python ytbmp3Server.py [OPTIONS] URL [URL ...]'
    else:
        YTB = YtbMP3Server()
        YTB.download(opts, args)
