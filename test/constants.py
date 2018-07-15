

FILE_NAME = 'src/rules.json'

INITIAL_KEY = 'rules_list'

KEYS_IN_RULES = ['action', 'condition', 'constraints']

VALUES_IN_CONDITION = ['all', 'any']

KEYS_IN_CONSTRAINTS = ['field_name', 'predicate', 'value']

VALUES_IN_FIELD_NAME = ['from', 'to', 'subject', 'date']

VALUES_IN_PREDICATE = ['contains', 'does not contains', 'equal', 'does not equal',
                       'lesser than days', 'lesser than months',
                       'greater than days', 'greater than months']

KEYS_IN_ACTION = ['mark', 'label']

VALUES_IN_MARK_ACTION = ['read', 'unread', 'archive']
