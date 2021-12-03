from secrets import choice

options = {
    'details': 'When the impostor is sus 😳',
    'buttons': [
        {
            'label': 'Ur mum',
            'url': 'https://lordronz.github.io/',
        },
        {
            'label': 'gae 😳',
            'url': 'https://lordronz.github.io/',
        },
    ],
    'start': 1,
    'state': 'ur mum gae',
    'party_size': [69, 420],
    'large_image': 'amogustwerk',
    'large_text': 'When the impostor is sus 😳',
    'small_image': 'amogus',
    'small_text': 'When the impostor is sus 😳',
}

assets = (
    'amogus',
    'amogustwerk',
    'jermasus',
    'mogus3d',
    'amogusdoge',
    'amogusobject0',
    'amogusobject1',
)

states = (
    'ligma balls',
    'ur mum gae',
    'deez nutz',
    'sugoma',
)

fun_nums = (69, 420, 1337)

details = (
    'When the impostor is sus 😳',
    'Get out of my head, get out of my head',
    'AAAAAAAAAAAAAAAAAAAA',
    'This is my kingdom come',
)

def get_options():
    return {
        'details': choice(details),
        'buttons': [
            {
                'label': 'Ur mum',
                'url': 'https://lordronz.github.io/',
            },
            {
                'label': 'gae 😳',
                'url': 'https://lordronz.github.io/',
            },
        ],
        'start': 1,
        'state': choice(states),
        'party_size': [choice(fun_nums), choice(fun_nums)],
        'large_image': choice(assets),
        'large_text': 'When the impostor is sus 😳',
        'small_image': choice(assets),
        'small_text': 'When the impostor is sus 😳',
    }
