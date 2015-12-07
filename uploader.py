#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Upload file in command line to GAE_CDN 
'''

UPLOAD_URL = 'http://<GAE_APP_ID>.appspot.com/upload.json'

from sys import argv
import json
import requests
import mimetypes
import random

class Uploader(object):
    def __init__(self, cdn_count=5):
        super(UploadToKACDN, self).__init__()
        self.cdn_count = cdn_count

    def upload(self, content, content_type='image/jpeg', filename='image.jpg'):
        files = {
            'file': (filename, content, content_type),
        }
        cdn_idx = '%02d'%(random.randrange(self.cdn_count)+1,)
        r = requests.get(UPLOAD_URL)
        print r.text
        try:
            url = json.loads(r.text).get('upload_url')
        except ValueError, e:
            return False
        r = requests.post(url, files=files)
        print r.text
        try:
            rv = json.loads(r.text)
        except ValueError:
            return False
        return rv.get('url', False)
        

if __name__=='__main__':
    sti = Uploader()
    fn = argv[1].split('/')[-1]
    ct = mimetypes.guess_type(fn)[0] or 'application/octet-stream'
    output = sti.upload(open(argv[1]), filename=fn, content_type=ct)
