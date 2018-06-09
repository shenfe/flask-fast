import json
from flask_restplus import fields
import os

script_dir = os.path.dirname(__file__)
mock_path = '../client/mock'


def read_json(path):
    path = os.path.join(script_dir, mock_path, path)
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        print 'Error: fail to read json file: ' + path
        return {}
    else:
        return {}


def is_basic(v):
    return isinstance(v, (str, unicode, int, float, bool)) or (v is None)


def traverse(obj):
    if isinstance(obj, dict):
        for key, value in obj.iteritems():
            # print [obj, key, value]
            if is_basic(value):
                yield obj, key, value
            else:
                for a, b, c in traverse(value):
                    yield a, b, c
    elif isinstance(obj, list):
        for key, value in enumerate(obj):
            if is_basic(value):
                yield obj, key, value
            else:
                for a, b, c in traverse(value):
                    yield a, b, c


def field_of(value):
    if isinstance(value, str):
        return fields.String(example=value)
    if isinstance(value, unicode):
        return fields.String(example=value.encode('utf-8'))
    if isinstance(value, int):
        return fields.Integer(example=value)
    if isinstance(value, float):
        return fields.Arbitrary(example=value)
    if isinstance(value, bool):
        return fields.Boolean(example=value)
    if isinstance(value, list):
        return fields.List(example=value)
    return fields.Nested(example=value)


def data_of(path):
    data = read_json(path)
    return data


def fields_of(path):
    data = read_json(path)
    # print path + ': ' + json.dumps(data)
    for target, key, value in traverse(data):
        # print target, key, value
        target[key] = field_of(value)
    return data
