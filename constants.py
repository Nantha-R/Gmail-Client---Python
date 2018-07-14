
class MailAttributes:
    """
    Class used for storing mail attributes.
    """
    READ_ONLY_SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'
    MODIFY_SCOPE = 'https://www.googleapis.com/auth/gmail.modify'
    CREDENTIALS = 'credentials.json'
    CLIENT_SECRET = 'client_secret.json'
    USER_ID = 'me'
    VERSION = 'v1'
    SERVICE = 'gmail'
    INBOX = 'inbox'


class DbAttributes:
    """
    Class used for storing Database attributes.
    """
    HOST_NAME = 'localhost'
    DATABASE_NAME = 'popo'
    TABLE_NAME = 'mail_contents'
    CONNECT_TIME_OUT = 5
    USER_NAME = 'popo'
    PASSWORD = 'popo'


class RulesAttributes:
    """
    Class used for storing Rules attributes.
    """
    STRING_TYPE_FIELDS = ['from', 'to', 'subject']

