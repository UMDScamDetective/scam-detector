#!/usr/bin/env python3

import email
import mailbox

from html.parser import HTMLParser

class EmailHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.parsed_content = ""

    def handle_data(self,data):
        self.parsed_content += data

# load and parse file
test_file = "./data/phishing1.mbox"
mbox = mailbox.mbox(test_file)

def handle_text_plain(msg):
    data = msg.get_payload()
    print("plain text: %s" % data[:40])

def handle_text_html(msg):
    data = msg.get_payload()
    parser = EmailHTMLParser()
    parser.feed(data)
    print("html text: %s" % parser.parsed_content[:40])

type_handlers = \
    { "text/plain": handle_text_plain
    , "text/html" : handle_text_html
    }
    
def default_handler(msg):
    print("Unknown message of type: %s" % msg.get_content_type())

def handle_message(msg,level):
    if msg.is_multipart():
        print( ">>>>" * level )
        for x in msg.get_payload():
            handle_message(x,level+1)
        print( "<<<<" * level )
    else:
        print("[Email begin]")
        handler = type_handlers.get(
                    msg.get_content_type(),
                    default_handler)
        handler(msg)
        print("[Email end]")

# handle each messages
for m in mbox:
    handle_message(m,0)
