import json
import os.path


def load(filename):
    with open(filename) as file:
        data = json.load(file)
    return data


def dump(obj, fullpath, sort_keys=True):
    with open(os.path.join(fullpath), 'w', encoding='utf8') as json_file:
        json.dump(obj, json_file, sort_keys=sort_keys,
                  indent=2, ensure_ascii=False)
        json_file.write('\n')
