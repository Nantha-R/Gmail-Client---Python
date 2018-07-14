import pymysql
from constants import DbAttributes


class DbHandler:
    """
    Class used for handling database related operations.
    """
    def __init__(self, no_of_emails):
        """
        Constructor for DbHandler.
        """
        self.no_of_emails = no_of_emails
        self.connection = self.__get_connection()

    def __get_connection(self):
        """
        Used for establishing database connection.
        :return: database connection.
        """
        try:
            conn = pymysql.connect(DbAttributes.HOST_NAME,
                                   user=DbAttributes.USER_NAME,
                                   passwd=DbAttributes.PASSWORD,
                                   db=DbAttributes.DATABASE_NAME,
                                   connect_timeout=DbAttributes.CONNECT_TIME_OUT)
            return conn
        except Exception as e:
            raise Exception(e)

    def insert_mail_contents(self, mail_contents):
        """
        Used for inserting records into the database.
        :param mail_contents: contents of the mail.
        :return: None
        """
        try:
            with self.connection.cursor() as cur:
                # On DUPLICATE KEY VALUE UPDATE used to make sure that all new entries are
                # inserted during batch insert and duplicate values are discarded.
                query = ("INSERT INTO {0} VALUES(%s,%s,%s,%s,%s)"
                         "ON DUPLICATE KEY UPDATE mail_id = mail_id"
                         .format(DbAttributes.TABLE_NAME))
                cur.executemany(query, mail_contents)
                self.connection.commit()
        except Exception as e:
            raise Exception(e)

    def retrieve_mail_contents(self):
        """
        Retrieve mail contents from the database.
        :return: mail contents.
        """
        try:
            with self.connection.cursor(pymysql.cursors.DictCursor) as cur:
                # ORDER BY is used to make sure that the first n records
                # are retrieved from the database.
                query = ("SELECT * FROM {0} ORDER BY mail_id LIMIT {1}"
                         .format(DbAttributes.TABLE_NAME, self.no_of_emails))
                cur.execute(query)
                return cur.fetchall()
        except Exception as e:
            raise Exception(e)
