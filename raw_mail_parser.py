#!/usr/bin/env python2

import email

test_file = "./data/phishing1.mbox"

with open(test_file, "r") as f:
    content = f.read()

msg = email.message_from_string(content)

for part in msg.walk():
    print part.get_content_type()
