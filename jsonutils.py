import json
import sys
import os


def parse_json(json_file):
    json_data = {}

    if(not os.path.isfile(json_file)):
        print(json_file, 'does not exists.')
        sys.exit(1)

    with open(json_file) as f:
        json_data = json.load(f)
    return json_data
