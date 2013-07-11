#!/usr/bin/env python

import imaplib
import smtplib
import sys
import getpass
import email.parser
import config
import errno

# connect to imap
print 'Connecting to %s as user %s ...' % (config.imaphost, config.username)
IMAP = imaplib.IMAP4_SSL

try:
    imap_server = IMAP(config.imaphost, config.imapport)
    if not config.password:
        config.password = getpass.getpass()
    imap_server.login(config.username, config.password)
except Exception, e:
    print 'Error:', e
    sys.exit(errno.ECONNREFUSED)
print "Connecting to SMTP"
# connect to smtp
try:
    smtp_server = smtplib.SMTP(config.smtphost, config.smtpport)
    if not config.password:
        config.password = getpass.getpass()
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.ehlo
    smtp_server.login(config.username, config.password)
except Exception, e:
    print 'Could not connect to', config.smtphost, e.__class__, e
    sys.exit(errno.ECONNREFUSED)

# filter unseen messages from the given folder
imap_server.select(config.folder)
resp, items = imap_server.search(None, "UNSEEN")
numbers = items[0].split()

# forward each message
sender = "%s@%s" % (config.username, config.imaphost)
for num in numbers:
    resp, data = imap_server.fetch(num, "(RFC822)")
    text = data[0][1]
    parser = email.parser.HeaderParser()
    msg = parser.parsestr(text)
    subject = "%(subject)s @%(notebook)s" %\
        {'subject': msg['Subject'], 'notebook': config.notebook_name}
    msg.replace_header('Subject', subject)
    text = msg.as_string()

    smtp_server.sendmail(sender, config.destination, text)

imap_server.close()
smtp_server.quit()
