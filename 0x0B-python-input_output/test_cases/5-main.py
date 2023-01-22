#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    filemame = "file_7"
    data = { 1, 2, 3 }
    save_to_json_file(data, filemame)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filemame = "no_perm/file_7"
    data = [1, 2, 3]
    save_to_json_file(data, filemame)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
