import bleach

ALLOWED_TAGS = ['b', 'i', 'u', 'a', 'p', 'strong', 'em']
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title']
}

def sanitize_input(user_input):
    return bleach.clean(user_input, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)
