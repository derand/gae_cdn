# Google App Engine CDN with 'Load balancer'

Simple CDN server on Google App Engine writen at Python. 

**_gae_cdn0x_** - GAE Application. This is one instance of CDN server. You can run one or more applications on GAE and switch between them with 'gae_cdn-balancer' application.

**_gae_cdn-balancer_** - Balancer GAE application. Redirect between **gae_cdn0x** applications.

**_uploader.py_** - example python script that upload file to CDN.

For working you should set google app id's at files:

+ _gae_cdn0x/app.yaml_ - GAE application id. This ID should ends with two digits ordinal number of application instance.
+ _gae_cdn-balancer/app.yaml_ 
+ _gae_cdn-balancer/main.py_ - 'GAE_APP_NAME' and 'cdn_count' variables

For example you want start cdn cluster with 3 instances named 'abc'. You should start 3 apps of _gae_cdn0x_ named: 'abc01', 'abc02' and 'abc03' and one app 'gae_cdn-balancer' with variables on _gae_cdn-balancer/main.py_:

    cdn_count = 3
    GAE_APP_NAME = 'abc'

Upload each file act in two steps. First get upload url (HTTP GET request to /upload.json) and second - upload file to url getted at first step.

## Licensing

This project is licensed under MIT License Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
