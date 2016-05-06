import os
import re
import sys, getopt

class YtbMP3Server:
    """docstring for YtbMP3Server"""
    def __init__(self):
        self.addresses = ''
        self.proxy = ''
        self.b = '320'

    def download(self, opts, args):
        for address in args:
            self.addresses += (' ' + address)

        for op, v in opts:
            if op == '-p':
                self.proxy = v
            elif op == '-b':
                slef.b = v

        print self.proxy
        if self.proxy == '':
            dl = os.popen('youtube-dl' + self.addresses).read()
        else:
            dl = os.popen('youtube-dl --proxy ' + self.proxy + self.addresses).read()
            # print os.path.dirname(os.path.realpath(__file__))

        downloadedFiles = []
        for dirPath, dirNames, fileNames in os.walk(os.path.dirname(os.path.realpath(__file__))):
            for fileName in fileNames:
                if os.path.splitext(fileName)[1] == '.mp4' or os.path.splitext(fileName)[1] == '.mkv':
                    print fileName
                    downloadedFiles.append(fileName)

        for file in downloadedFiles:
            os.popen('lame -b ' + self.b + ' ' + file)


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'p:b:')
    if len(sys.argv) < 2:
        print u'Usage: python ytbmp3Server.py [OPTIONS] URL [URL ...]'
    else:
        YTB = YtbMP3Server()
        YTB.download(opts, args)
