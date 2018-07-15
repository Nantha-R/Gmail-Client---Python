import json
from utilities import *
from constants import RulesAttributes


class RulesParser:
    """
    Class used for parsing the set of rules.
    """
    def __parse_rules(self, data):
        """
        Used for parsing the rules from rules.json
        :param data: data read from rules.json.
        :return: rules.
        """
        rules_content = []
        rules_list = data['rules_list']
        for rule in rules_list:
            rule_content = {
                "condition": rule.get('condition'),
                "constraints": rule.get('constraints'),
                "action": rule.get('action')
            }
            rules_content.append(rule_content)
        return rules_content

    def __get_rules(self):
        """
        Used for retrieving the rules from rules.json.
        :return: rules present in the json file.
        """
        try:
            with open('rules.json') as file:
                data = json.loads(file.read())
            rules = self.__parse_rules(data)
            return rules
        except Exception as e:
            raise Exception(e)

    def __check_constraint(self, mail, constraint):
        """
        Check if the mail satisfies the given constraint.
        :param mail: contents of the mail.
        :param constraint: constraint of the rule.
        :return: None
        """
        field_name = constraint['field_name']
        if field_name in RulesAttributes.STRING_TYPE_FIELDS:
            # The below functions are defined in utilities.py.
            switcher = {
                "contains": contains,
                "does not contains": not contains,
                "equals": equal_to,
                "does not equal": not equal_to
            }
            return switcher.get(constraint['predicate'])(constraint['value'], mail[field_name])
        else:
            # The below functions are defined in utilities.py.
            switcher = {
                "lesser than days": lesser_than_days,
                "greater than days": greater_than_days,
                "lesser than months": lesser_than_months,
                "greater than months": greater_than_months
            }
            return switcher.get(constraint['predicate'])(constraint['value'], mail[field_name])

    def __get_action(self, mail, rule):
        """
        Get the action to be performed for the mail.
        :param mail: contents of particular mail.
        :param rule: contents of particular rule.
        :return: action list.
        """
        condition = rule['condition']
        action = rule['action']
        for constraint in rule['constraints']:
            result = self.__check_constraint(mail, constraint)
            if condition == 'all':
                if not result:
                    return None
            elif condition == 'any':
                if result:
                    # Found a constraint in the rule that match the mail.
                    return action
        if condition == 'all':
            # Found a constraint in the rule that match the mail.
            return action
        else:
            return None

    def get_actions(self, mail_contents):
        """
        Used for processing actions to be performed on each mail.
        :param mail_contents: contains mail contents to be processed.
        :return: mail id and its related action to be performed.
        """
        result = []
        rules = self.__get_rules()
        for mail in mail_contents:
            for rule in rules:
                actions = self.__get_action(mail, rule)
                if actions is not None:
                    # Found a mail that match the given rule.
                    result.append({
                        'mail_id': mail['mail_id'],
                        'actions': actions
                    })
                    break
        return result
