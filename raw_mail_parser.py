#!/usr/bin/env python2

import email
import mailbox

from HTMLParser import HTMLParser

class EmailHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.parsed_content = ""

    def handle_data(self,data):
        self.parsed_content += data

# load and parse file
test_file = "./data/phishing1.mbox"
mbox = mailbox.mbox(test_file)

def handle_text_plain(data):
    print "Encounter plain text: %s" % data[:10]

def handle_text_html(data):
    parser = EmailHTMLParser()
    parser.feed(data)
    print parser.parsed_content

type_handlers = \
    { "text/plain": handle_text_plain
    , "text/html" : handle_text_html
    }

def handle_message(msg):
    if msg.is_multipart():
        # TODO: what are these messages?
        print "<multimple messages>"
    else:
        print "--------- New email"
        type_handlers[msg.get_content_type()](msg.get_payload())

interesting_msgs = \
    filter(lambda x: not x.is_multipart(), mbox)

# handle each messages
map(handle_message, interesting_msgs)
