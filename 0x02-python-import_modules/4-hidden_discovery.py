#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    name_list = dir(hidden_4)
    for name in name_list:
        if name[:2] != '__':
            print("{}".format(name))
