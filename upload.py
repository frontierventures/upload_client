from twisted.internet import defer
from twisted.internet import reactor
from twisted.web import client
from twisted.web import http_headers

import producer
import receiver


def finished(bytes):
    print "Upload DONE: %d" % bytes


def progress(current, total):
    print "Upload PROGRESS: %d out of %d" % (current, total)


def error(error):
    print "Upload ERROR: %s" % error


def responseDone(data):
    print "Response:"
    print "-" * 80
    print data
    reactor.stop()


def responseError(data):
    print "ERROR with the response. So far I've got:"
    print "-" * 80
    print data
    reactor.stop()

#url = "http://kramer/upload.php"
url = "http://50.116.15.78:8080"
#    dd if=/dev/zero of=file.txt count=1024 bs=1024
files = {
    "upload": "/root/workspace-python/file.txt"
}
data = {
    "field1": "value1"
}

producerDeferred = defer.Deferred()
producerDeferred.addCallback(finished)
producerDeferred.addErrback(error)

receiverDeferred = defer.Deferred()
receiverDeferred.addCallback(responseDone)
receiverDeferred.addErrback(responseError)

myProducer = producer.MultiPartProducer(files, data, progress, producerDeferred)
myReceiver = receiver.StringReceiver(receiverDeferred)

headers = http_headers.Headers()
headers.addRawHeader("Content-Type", "multipart/form-data; boundary=%s" % myProducer.boundary)

agent = client.Agent(reactor)
request = agent.request("POST", url, headers, myProducer)
request.addCallback(lambda response: response.deliverBody(myReceiver))

reactor.run()
