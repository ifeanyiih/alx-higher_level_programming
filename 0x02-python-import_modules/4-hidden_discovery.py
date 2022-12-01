#!/usr/bin/python3


def print_hidden(hidden):
    for name in hidden:
        if not name.startswith('__'):
            print(name)


if __name__ == '__main__':
    import hidden_4
    print_hidden(dir(hidden_4))
