import urllib2

class YtbMP3Local:
    """docstring for YtbMP3Local"""
    def __init__(self):
        self.html = ''
        self.port = '23333'

    def getHTML(self, url):
        self.html = urllib2.Request(url + ':' + self.port)

    def getMP3(self, opts, args):
        for address in args:
            self.addresses += (' ' + address)

        for op, v in opts:
            if op == '-p':
                self.proxy = v
        #     elif op == '-b':
        #         slef.b = v

        if self.proxy == '':
            dl = os.popen('youtube-dl' + self.addresses).read()
        else:
            dl = os.popen('youtube-dl --proxy ' + self.proxy + self.addresses).read()

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
            os.popen('lame -b ' + self.b + ' ' + '"' + file + '"')
            os.popen('rm ' + '"' + file + '"')
            c += 1
            print str(c / l * 100) + '%   ' + '(' + str(c) + '/' + str(int(l)) + ')'


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'p:')
    if len(sys.argv) < 2 or len(args) > 1:
        print u'Usage: python ytbmp3Local.py [OPTIONS] IP'
    else:
        YTB = YtbMP3Local()
        YTB.getHTML(args[0])
        YTB.getMP3(opts, args)
