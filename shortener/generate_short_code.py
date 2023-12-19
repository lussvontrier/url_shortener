from hashlib import md5
from string import ascii_letters
from random import choice

from django.conf import settings


def generate_short_code():
    code = ''.join([
        choice(ascii_letters) for _ in range(settings.MAX_LENGTH_SHORT_URL)
    ])
    new_code = md5(code.encode()).hexdigest()[:settings.MAX_LENGTH_SHORT_URL]
    return new_code
