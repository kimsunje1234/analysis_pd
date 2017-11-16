import os

# configuration
CONFIG = {
    'district': '서울특별시',
    'countries': [('중국', 112), ('일본', 130), ('미국', 275)],
    'common': {
        'service_key': 'cPQKd56v%2BVVNJkYiFQAQlUx3goMifIQV5MajwQZbEZk%2F%2BmM84tizuja2ZqkIRjzxjU7bbk8bbjW1dJ2yffa%2F7w%3D%3D',
        'start_year': 2015,
        'end_year': 2017,
        'restore_directory': '__results__/crawling',
        'fetch': True
    }
}

if not os.path.exists(CONFIG['common']['restore_directory']):
    os.makedirs(CONFIG['common']['restore_directory'])