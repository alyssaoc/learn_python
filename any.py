items = [0, None, 0.0, True, 0, 7]
def any(items):
    for item in items:
        print('scanning item', item)
        if item:
            print('At least one item evaluates to True')
    print('All items evaluate to False')
