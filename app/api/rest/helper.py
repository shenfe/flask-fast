import json
from app.util.common import read_json, traverse
from flask_restplus import fields, reqparse

from app.api import api


__mod_counter = 0


def __gen_mod_name():
    global __mod_counter
    __mod_counter += 1
    return '__AnonymousModel' + str(__mod_counter)


def Mod(*args, **kwargs):
    name = args[0]
    if not isinstance(name, str):
        name = __gen_mod_name()
        return api.model(name, *args, **kwargs)
    return api.model(*args, **kwargs)


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
        return fields.List(field_of(value[0]))
    return fields.Nested(Mod({
        key: field_of(val) for (key, val) in value.items()
    }))


__mock_path = 'client/mock'


def data_of(path):
    return read_json(__mock_path, path)


def fields_of(path, as_file=True):
    data = data_of(path) if as_file else path
    for target, key, value in traverse(data):
        target[key] = field_of(value)
    return data


__mock_mods = {}


def mock_mod(json_name, mod_name=None):
    if mod_name is None:
        mod_name = json_name
    mod = None
    if mod_name in __mock_mods:
        mod = __mock_mods[mod_name]
    else:
        __mock_mods[mod_name] = Mod(mod_name, fields_of(json_name + '.json'))
        mod = __mock_mods[mod_name]
    # print(mod)
    return mod


def mock_data(json_name):
    return data_of(json_name + '.json')


def gen_parser(data_sample, location='path'):
    """Generate a parser.

    Args:
        data_sample: sample data.
        location: argument location, see [Source code for flask_restplus.reqparse](https://flask-restplus.readthedocs.io/en/stable/_modules/flask_restplus/reqparse.html?highlight=RequestParser) for more.

    Returns:
        An argument parser, created by `api.parser()`.
    """
    parser = reqparse.RequestParser()
    for name, value in data_sample.items():
        parser.add_argument(name, type=type(value), default=value, location=location)
    return parser


def query_parser(data_sample):
    return gen_parser(data_sample)


def form_parser(data_sample):
    return gen_parser(data_sample, location='form')

