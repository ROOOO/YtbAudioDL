import os
import re
import sys, getopt

class YtbAudioServer:
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
            dl = os.popen('youtube-dl -x --audio-quality 0 ' + self.addresses).read()
        else:
            # dl = os.popen('youtube-dl -x --audio-quality 0 --proxy ' + self.proxy + self.addresses).readline()
            dl = os.popen('youtube-dl --proxy ' + '"' + self.proxy + '"' + self.addresses).read()

        # self.HTTPServer()

    def HTTPServer(self):
        try:
            os.popen('python -m SimpleHTTPServer 23333 &')
        except:
            pass

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'p:')
    if len(sys.argv) < 2:
        print u'Usage: python ytbmp3Server.py [OPTIONS] URL [URL ...]'
    else:
        YTB = YtbAudioServer()
        YTB.download(opts, args)
