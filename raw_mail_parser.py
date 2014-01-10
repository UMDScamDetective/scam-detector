#!/usr/bin/env python2

import email

test_file = "./data/phishing1.mbox"

with open(test_file, "r") as f:
    msg = email.message_from_file(f)

for k,v in msg.items():
    print "%s ====> %s" % (k,v)

print msg.get_payload()[:1000]
