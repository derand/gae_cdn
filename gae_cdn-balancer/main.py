import urllib
import webapp2
import json
import random

cdn_count = 5
cdn_last_idx = None
GAE_APP_NAME = '<GAE_APP_ID>'

class MainHandler(webapp2.RequestHandler):
    def get(self):
        respond = self.response.out.write
        page = '<html><body>'
        page += self.request.host_url
        page += '</body></html>'
        respond(page)

class UploadHandler(webapp2.RequestHandler):
    def get(self):
        global cdn_count
        global cdn_last_idx
        global GAE_APP_NAME
        if cdn_last_idx and cdn_count > 1:
            cdn_idx = random.randrange(cdn_count-1)+1
            if cdn_idx >= cdn_last_idx:
                cdn_idx += 1
        else:
            cdn_idx = random.randrange(cdn_count)+1
        cdn_last_idx = cdn_idx
        url = 'http://%s%02d.appspot.com/upload.json'%(GAE_APP_NAME, cdn_idx)
        self.redirect(url)

app = webapp2.WSGIApplication(
            [('/', MainHandler),
             ('/upload.json', UploadHandler),
            ], debug=False)
