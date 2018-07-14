from oauth2client import file, client, tools
from constants import MailAttributes
from httplib2 import Http
from googleapiclient.discovery import build
from dateutil.parser import *
from googleapiclient import errors


class MailHandler:
    """
    Class used for performing mail handling operations.
    """
    def __init__(self, no_of_emails):
        """
        Constructor for MailHandler.
        :param no_of_emails: Number of emails to be processed per run.
        """
        self.no_of_emails = no_of_emails
        self.mail_client = self.__initiate_mail_client()

    def __initiate_mail_client(self):
        """
        Used for initiating the mail client.
        :return: mail_client.
        """
        store = file.Storage(MailAttributes.CREDENTIALS)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(MailAttributes.CLIENT_SECRET,
                                                  MailAttributes.MODIFY_SCOPE)
            credentials = tools.run_flow(flow, store)
        mail_client = build(MailAttributes.SERVICE,
                            MailAttributes.VERSION,
                            http=credentials.authorize(Http()))
        return mail_client

    def __parse_mail(self, mail_response, mail_id):
        """
        Used for parsing mail contents.
        :param mail_response: http response containing all information about a particular email.
        :return: contents of a mail.
        """
        headers = mail_response['payload']['headers']
        for header in headers:
            header_name = header['name']
            if header_name == 'Subject':
                subject = header['value']
            elif header_name == 'Date':
                # Convert date into datetime object.
                date = parse(header['value']).date()
            elif header_name == 'From':
                sender = header['value']
            elif header_name == 'To':
                receiver = header['value']
        return (mail_id, sender, receiver, subject, date)

    def retrieve_emails(self):
        """
        Used for retrieving the list of emails.
        :return: message_list.
        """
        try:
            # Retrieve a list of email information.
            mail_response = self.mail_client.users().messages().list(userId=MailAttributes.USER_ID,
                                                                     maxResults=self.no_of_emails).execute()
            mail_list = mail_response['messages']
            mail_contents = []

            for mail in mail_list:
                # Get contents of email one by one.
                mail_response = self.mail_client.users().messages().get(userId=MailAttributes.USER_ID,
                                                                        id=mail['id']).execute()
                mail_contents.append(self.__parse_mail(mail_response, mail['id']))

            return mail_contents

        except errors.HttpError as error:
            raise Exception(error)

    def __mark_as_read(self, mail_id):
        """
        Used to mark the messages read.
        :param mail_id: id of the mail.
        :return: None
        """
        body_labels = {'removeLabelIds': ['UNREAD']}
        try:
            self.mail_client.users().messages().modify(userId=MailAttributes.USER_ID,
                                                       id=mail_id,
                                                       body=body_labels).execute()
        except errors.HttpError as error:
            raise Exception(error)

    def __mark_as_unread(self, mail_id):
        """
        Used to mark the messages unread.
        :param mail_id: id of the mail.
        :return: None
        """
        body_labels = {'addLabelIds': ['UNREAD']}
        try:
            self.mail_client.users().messages().modify(userId=MailAttributes.USER_ID,
                                                       id=mail_id,
                                                       body=body_labels).execute()
        except errors.HttpError as error:
            raise Exception(error)

    def __mark_as_archive(self, mail_id):
        """
        Mark the given mail as archive.
        :param mail_id: id of the mail.
        :return: None
        """
        body_labels = {'removeLabelIds': ['INBOX']}
        try:
            self.mail_client.users().messages().modify(userId=MailAttributes.USER_ID,
                                                       id=mail_id,
                                                       body=body_labels).execute()
        except errors.HttpError as error:
            raise Exception(error)

    def __label_mail(self, mail_id, label_name, labels):
        """
        Assign a label to the given mail.
        :param mail_id: Id of the mail.
        :param label_name: name of the label.
        :param labels: Set of labels present in the user gmail account.
        :return: None
        """
        label_id = None
        for label in labels:
            if label['name'] == label_name:
                label_id = label['id']
                break
        if label_id is not None:
            body_labels = {'addLabelIds': [label_id]}
            try:
                self.mail_client.users().messages().modify(userId=MailAttributes.USER_ID,
                                                           id=mail_id,
                                                           body=body_labels).execute()
            except errors.HttpError as error:
                raise Exception(error)

    def __get_labels(self):
        """
        Retrieve all labels from the gmail account.
        :return: label informations.
        """
        try:
            response = self.mail_client.users().labels().list(userId=MailAttributes.USER_ID).execute()
            return response['labels']
        except errors.HttpError as error:
            raise Exception(error)

    def perform_action(self, result_set):
        """
        Used for performing actions to the mails that match the given rules.
        :param result_set: Contains mail id and its actions to be performed.
        :return: None
        """
        # Get the label information from the gmail account.
        labels = self.__get_labels()
        for result in result_set:
            mail_id = result['mail_id']
            actions = result['actions']
            switcher = {
                'read': self.__mark_as_read,
                'unread': self.__mark_as_unread,
                'archive': self.__mark_as_archive
            }
            for action in actions:
                for key, value in action.items():
                    if key == 'mark':
                        switcher.get(value)(mail_id)
                    elif key == 'label':
                        self.__label_mail(mail_id, value, labels)
