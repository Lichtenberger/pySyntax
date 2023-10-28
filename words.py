names = ['joe', 'mike', 'tom', 'earl', 'pete']

def print_upper_words(name):
    '''Reformats to uppercase'''
    for name in names:
        if name.startswith('e' or 'm'):
            print name.upper()

