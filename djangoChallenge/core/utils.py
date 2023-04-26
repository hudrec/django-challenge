def generate_shorted_url(num):
    ALPHABET = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    if num == 0:
        return ALPHABET[0]

    s = ''
    base = len(ALPHABET)
    while num > 0:
        s = s + ALPHABET[num % base]
        num = num // base

    return s[::-1]
