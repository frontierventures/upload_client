#!/usr/bin/env python
from twisted.web.template import Element, renderer
from twisted.web.template import XMLString


class FileUpload(Element):
    loader = XMLString('''
                       <div xmlns:t="http://twistedmatrix.com/ns/twisted.web.template/0.1" t:render="form">
                       <form action="" method="POST" enctype="multipart/form-data">
                       <input type="hidden" name="foo" value="bar"></input>
                       <input type="hidden" name="file_foo" value="not a file"></input>
                       file_foo: <input type="file" name="file_foo"></input>
                       file_foo: <input type="file" name="file_foo"></input>
                       file_bar: <input type="file" name="file_bar"></input>
                       <input type="submit" value="submit"></input>
                       </form>
                       </div>
                        ''')

    @renderer
    def form(self, request, tag):
        return tag
