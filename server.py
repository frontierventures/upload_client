#!/usr/bin/env python
from twisted.web.server import Site, NOT_DONE_YET
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.python import log

from twisted.web.template import flattenString
#from element import ExampleElement
import element
import sys


class Root(Resource):
    isLeaf = True

    def render(self, request):
        request.write("<!DOCTYPE html>\n")
        request.write("<!DOCTYPE html>\n")
        request.write("<html>\n")
        request.write("<head>\n")
        request.write("<meta charset=\"utf-8\">\n")
        request.write("<title></title>\n")
        request.write("<meta name=\"description\" content=\"\">\n")
        request.write("</head>\n")
        request.write("<body>\n")
        print request.args
        #flattenString(request, ExampleElement()).addCallback(request.write)
        flattenString(request, element.FileUpload()).addCallback(request.write)
        request.write("</body>\n")
        request.write("</html>\n")
        request.finish()
        return NOT_DONE_YET

log.startLogging(sys.stdout)

root = Root()
root.putChild('', root)
#root.putChild('register', register.Main())

site = Site(root)

reactor.listenTCP(8080, site)
reactor.run()
