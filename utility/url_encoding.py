
def encode_url(url_string):
    return url_string.replace(' ', '_')

def decode_url(url_string):
    return url_string.replace('_', ' ')
