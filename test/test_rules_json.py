import json
from test import constants

data = None
rules = None


def test_json():
    """
    Used for testing if the rules.json is of valid JSON format.
    :return: None
    """
    try:
        global data
        with open(constants.FILE_NAME) as file:
            data = json.loads(file.read())
    except ValueError:
        assert False, "The given JSON is not of valid format."
    except OSError:
        assert False, "The given rules.json is not present."


def test_keys_in_json():
    """
    Used for checking the key values given in JSON.
    :return: None
    """
    global data, rules
    # Check for initial key 'rules_list'.
    keys = list(data.keys())
    if keys != [constants.INITIAL_KEY]:
        assert False, "Only rules_list should be present as the initial key."

    # Check for keys inside each rules.
    rules = data[constants.INITIAL_KEY]
    for rule in rules:
        if sorted(list(rule.keys())) != constants.KEYS_IN_RULES:
            assert False, ("Error in rule ({0})."
                           "Only these keys should be used for each rules : ({1})."
                           .format(rule, ','.join(constants.KEYS_IN_RULES)))


def test_condition_in_rules():
    """
    Used to check whether the condition specified in rules.json is correct.
    :return: None
    """
    global rules
    for rule in rules:
        if rule['condition'] not in constants.VALUES_IN_CONDITION:
            assert False, ("Error in rule ({0})"
                           "Only these values should be assigned to each condition : ({1})"
                           .format(rule, ','.join(constants.VALUES_IN_CONDITION)))


def test_constraint_in_rules():
    """
    Used to check the constraints specified in each rule.
    :return: None.
    """
    global rules
    for rule in rules:
        for constraint in rule['constraints']:
            if sorted(list(constraint.keys())) != constants.KEYS_IN_CONSTRAINTS:
                assert False, ("Error in rule ({1})"
                               "Only these keys should be assigned to each constraint : ({1})"
                               .format(rule, ','.join(constants.KEYS_IN_CONSTRAINTS)))

            if constraint['field_name'] not in constants.VALUES_IN_FIELD_NAME:
                assert False, ("Error in rule ({0})"
                               "Only these values should be assigned to each field_name : ({1})"
                               .format(rule, ','.join(constants.VALUES_IN_FIELD_NAME)))

            if constraint['predicate'] not in constants.VALUES_IN_PREDICATE:
                assert False, ("Error in rule ({0})"
                               "Only these values should be assigned to each predicate : ({1})"
                               .format(rule, ','.join(constants.VALUES_IN_PREDICATE)))

            if constraint['field_name'] == 'date':
                try:
                    num = int(constraint['value'])
                except ValueError:
                    assert False, ("Error in rule ({0})"
                                   "Only integer vales should be assigned."
                                   .format(rule))


def test_action_in_rules():
    """
    Used for testing action field in rules.
    :return: None
    """
    global rules
    for rule in rules:
        for action in rule['action']:
            keys = list(action.keys())
            if len(keys) != 1:
                assert False, ("Error in rule ({})"
                               "Only one action should be specified in a dict"
                               .format(rule))
            if keys[0] not in constants.KEYS_IN_ACTION:
                assert False, ("Error in rule ({0})"
                               "Only these keys should be assigned to actions ({1})"
                               .format(rule, ','.join(constants.KEYS_IN_ACTION)))

            values = list(action.values())
            if len(values) != 1:
                assert False, ("Error in rule ({})"
                               "Only one action type should be specified in a dict"
                               .format(rule))
            if keys[0] == 'mark' and values[0] not in constants.VALUES_IN_MARK_ACTION:
                assert False, ("Error in rule ({0})"
                               "Only these values should be assigned to actions ({1})"
                               .format(rule, ','.join(constants.VALUES_IN_MARK_ACTION)))

