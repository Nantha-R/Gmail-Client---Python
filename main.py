from argparse import ArgumentParser
from mail_handler import MailHandler
from db_handler import DbHandler
from rules_parser import RulesParser

if __name__ == '__main__':
    # Sample command line for the script
    # python main.py -action read/perform_actions -number_of_emails 10
    # Parsing command line parameters
    parser = ArgumentParser()
    parser.add_argument('-a', '--action', dest='action', required=True, choices=['read', 'perform_actions'])
    parser.add_argument('-n', '--no_of_emails', dest='no_of_emails', default=10)
    arguments = parser.parse_args()

    action = arguments.action
    no_of_emails = arguments.no_of_emails

    mail_handler = MailHandler(no_of_emails)
    db_handler = DbHandler(no_of_emails)
    if action == 'read':
        # Read messages from INBOX.
        mail_contents = mail_handler.retrieve_emails()
        # Insert messages into the database.
        db_handler.insert_mail_contents(mail_contents)
    else:
        # Read messages from the database.
        mail_contents = db_handler.retrieve_mail_contents()
        # result_set contains mail id and the set of actions to be performed on them.
        result_set = RulesParser().get_actions(mail_contents)
        # Perform actions based on rules.
        mail_handler.perform_action(result_set)
    db_handler.connection.close()
