bills-to-evernote
=================

This is a local replacement for IFTTT who can't forward attachments as an attached file. 
The initial purpose is to forward all mails with "Bill" label to a specified Evernote notebook.


Usage
=====

1) Setup config.py 
- username & password for gmail 
- folder name in gmail which will be monitored for new mails to send to Evernote
- destination, Evernote email address for your account (You can check that in account info *@m.evernote.com

2) python app.py (Or start it with cron)

My Workflow
===========

I've created the script to automatically backup pdf bills sent to my email. Technically you can just forward them with a filter in gmail itself, but unfortunately, they will get into your evernote inbox, which I think is not right :)
The script fetches all unread mails from the folder, modifies the subject(adding @Notebook), and sends a mail. This way the workflow to archive bills(or anything else) is completely automated.
