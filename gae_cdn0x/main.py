import urllib
import webapp2
from google.appengine.ext import blobstore, db
from google.appengine.ext.blobstore import BlobInfo
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import memcache
import datetime
import json
import mimetypes

class FileRecord(db.Model):
    blob = blobstore.BlobReferenceProperty()
    md5 = db.StringProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        respond = self.response.out.write
        page = '<html><body>'
        page += self.request.host_url
        page += '</body></html>'
        respond(page)

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def get(self):
        upload_url = blobstore.create_upload_url('/upload.json')
        self.response.out.write('{"upload_url": "%s"}'%upload_url)

    def post(self):
        rv = { 'code': 500, 'message': 'Something going wrong'}
        uplds = self.get_uploads('file')
        if len(uplds) == 0:
            rv['message'] = 'Missing file data'
        blob_info = uplds[0]   # 'file' is file upload field in the form

        record = None
        if blob_info.md5_hash:
            record = db.Query(FileRecord).filter('md5 =', blob_info.md5_hash).get()

        if not record:
            record = FileRecord(blob=blob_info, md5=blob_info.md5_hash)
            try:
                record.put()
            except Exception, e:
                pass

        url = '%s/%s/%s'%(self.request.host_url, record.key().id(), urllib.quote(record.blob.filename))
        rv = {
            'code': 200,
            'url': url,
        }
        self.response.out.write(json.dumps(rv))

class GetHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, blob_key, fn):
        record = FileRecord.get_by_id(int(blob_key))
        if not record:
            self.error(404)
        else:
            if record.blob.content_type == 'application/octet-stream':
                self.response.headers['Content-Type'] = mimetypes.guess_type(record.blob.filename)[0] or 'application/octet-stream'
            else:
                self.response.headers['Content-Type'] = record.blob.content_type
            self.send_blob(record.blob, content_type=self.response.headers['Content-Type'])

app = webapp2.WSGIApplication(
            [('/', MainHandler),
             ('/upload.json', UploadHandler),
             ('/([^/]+)/([^/]+)?', GetHandler),
            ], debug=False)
