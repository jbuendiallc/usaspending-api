from usaspending_api.awards.v2.lookups.lookups import award_type_mapping

AWARD_FILTER = [
    {'name': 'award_ids', 'type': 'array', 'array_type': 'integer'},
    {'name': 'award_type_codes', 'type': 'enum', 'enum_values': award_type_mapping.keys()},
    {'name': 'contract_pricing_type_codes', 'type': 'array', 'array_type': 'text', 'text_type': 'search'},
    {'name': 'extent_competed_type_codes', 'type': 'array', 'array_type': 'text', 'text_type': 'search'},
    {'name': 'keyword', 'type': 'text', 'text_type': 'search'},
    {'name': 'legal_entities', 'type': 'array', 'array_type': 'integer'},
    {'name': 'naics_codes', 'type': 'array', 'array_type': 'text', 'text_type': 'search'},
    {'name': 'program_numbers', 'type': 'array', 'array_type': 'text', 'text_type': 'search'},
    {'name': 'psc_codes', 'type': 'array', 'array_type': 'text', 'text_type': 'search'},
    {'name': 'recipient_scope', 'type': 'enum', 'enum_values': ('domestic', 'foreign')},
    {'name': 'recipient_search_text', 'type': 'array', 'array_type': 'text', 'text_type': 'search', 'max': 1, 'min': 1},
    {'name': 'recipient_type_names', 'type': 'array', 'array_type': 'text', 'text_type': 'search'},
    {'name': 'set_aside_type_codes', 'type': 'array', 'array_type': 'text', 'text_type': 'search'},
    {'name': 'place_of_performance_scope', 'type': 'enum', 'enum_values': ['domestic', 'foreign']},
    {
        'name': 'time_period',
        'type': 'array',
        'array_type': 'object',
        'object_keys': {
            'start_date': {'type': 'date', 'optional': False},
            'end_date': {'type': 'date', 'optional': False}
        },
        'min': 1,
    },
    {
        'name': 'award_amounts',
        'type': 'array',
        'array_type': 'object',
        'object_keys': {
            'lower_bound': {'type': 'float', 'optional': True},
            'upper_bound': {'type': 'float', 'optional': True}
        },
        'min': 1,

    },
    {
        'name': 'agencies',
        'type': 'array',
        'array_type': 'object',
        'object_keys': {
            'type': {'type': 'enum', 'enum_values': ['funding', 'awarding'], 'optional': False},
            'tier': {'type': 'enum', 'enum_values': ['toptier', 'subtier'], 'optional': False},
            'name': {'type': 'text', 'text_type': 'search', 'optional': False}
        },
        'min': 1,

    },
    {
        'name': 'recipient_locations',
        'type': 'array',
        'array_type': 'object',
        'object_keys': {
            'country': {'type': 'text', 'text_type': 'search', 'optional': False},
            'state': {'type': 'text', 'text_type': 'search', 'optional': True},
            'zip': {'type': 'text', 'text_type': 'search', 'optional': True},
            'district': {'type': 'text', 'text_type': 'search', 'optional': True},
            'county': {'type': 'text', 'text_type': 'search', 'optional': True},
        },
        'min': 1,

    },
    {
        'name': 'place_of_performance_locations',
        'type': 'array',
        'array_type': 'object',
        'object_keys': {
            'country': {'type': 'text', 'text_type': 'search', 'optional': False},
            'state': {'type': 'text', 'text_type': 'search', 'optional': True},
            'zip': {'type': 'text', 'text_type': 'search', 'optional': True},
            'district': {'type': 'text', 'text_type': 'search', 'optional': True},
            'county': {'type': 'text', 'text_type': 'search', 'optional': True},
        },
        'min': 1,

    },

]

for a in AWARD_FILTER:
    a['optional'] = a.get('optional', True)  # want to make/keep time_period required
    a['key'] = 'filters|{}'.format(a['name'])
