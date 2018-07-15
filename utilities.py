import datetime
from dateutil import relativedelta

def contains(value, field):
    """
    Used to check if the value exists in the field.
    :param value: value in constraints.
    :param field: value in mail.
    :return: Boolean value
    """
    return value in field


def equal_to(value, field):
    """
    Used to check if value equals field.
    :param value: value in constraints.
    :param field: value in mail.
    :return: Boolean value
    """
    return value == field


def greater_than_days(value, field):
    """
    Used to compare dates using days.
    :param value: date in constraints.
    :param field: date in mail.
    :return: Boolean value
    """
    current_date = datetime.datetime.now().date()
    if (current_date - field).days >= int(value):
        return True
    else:
        return False


def lesser_than_days(value, field):
    """
    Used to compare dates using days.
    :param value: date in constraints.
    :param field: date in mail.
    :return: Boolean value
    """
    current_date = datetime.datetime.now().date()
    if (current_date - field).days <= int(value):
        return True
    else:
        return False


def greater_than_months(value, field):
    """
    Used to compare dates using months.
    :param value: date in constraints.
    :param field: date in mail.
    :return: Boolean value
    """
    current_date = datetime.datetime.now().date()
    if relativedelta.relativedelta(current_date, field).months >= int(value):
        return True
    else:
        return False


def lesser_than_months(value, field):
    """
    Used to compare dates using months.
    :param value: date in constraints.
    :param field: date in mail.
    :return: Boolean value
    """
    current_date = datetime.datetime.now().date()
    if relativedelta.relativedelta(current_date, field).months <= int(value):
        return True
    else:
        return False
