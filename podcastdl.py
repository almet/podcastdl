import errno
import os.path
import sys

import feedparser
import requests
from progressbar import Bar, Percentage, FileTransferSpeed, ProgressBar


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST or not os.path.isdir(path):
            raise


def get_media_elements(url):
    """Return all media elements from an url"""
    d = feedparser.parse(url)
    for entry in d.entries:
        mp3s = [l['href'] for l in entry['links'] if l['href'].endswith('mp3')]
        yield entry['title'], mp3s[0]


def download_track(title, url, output):
    """Download an url and display a progressbar"""
    local_filename = os.path.join(output, url.split('/')[-1])
    r = requests.get(url, stream=True)
    size = int(r.headers['Content-Length'].strip())
    _bytes = 0
    widgets = [title, ": ", Bar(marker="|", left="[", right=" "),
               Percentage(), " ",  FileTransferSpeed(), "] ",
               " of {0}MB".format(str(round(size / 1024 / 1024, 2))[:4])]

    pbar = ProgressBar(widgets=widgets, maxval=size).start()
    with open(local_filename, 'wb') as f:
        for buf in r.iter_content(1024):
            if buf:
                f.write(buf)
                _bytes += len(buf)
                pbar.update(_bytes)
                f.flush()
        pbar.finish()


def main():
    if len(sys.argv) < 2:
        print "Please specify the feed url you want to download."
        print "Usage: %s url" % sys.argv[0]
        return
    if len(sys.argv) > 2:
        output = sys.argv[2]
        mkdir_p(output)
    else:
        output = '.'
    for title, url in get_media_elements(sys.argv[1]):
        download_track(title, url, output)

if __name__ == '__main__':
    main()
