# Gmail-Client-Python
Gmail Client using Google GMAIL API in python.

1) Authenticate to Google’s GMail API using OAuth (use Google’s official Python client) and
   fetch a list of emails from the Inbox.
2) Store these emails into local MYSQL Database.
3) Now take action on each of these emails using rules given in the rules.json file.
4) Rules.json file contains actions to be done on each email based on its contents.
   for eg. Archive all emails that have the word 'abc' in their subject.
           Mark all emails that are two days old as read or unread.
           Add new label 'work' to all messages that are received from a mail id.

Reference : https://developers.google.com/gmail/api/v1/reference/users
