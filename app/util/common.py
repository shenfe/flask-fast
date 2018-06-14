import json
import os

script_dir = os.path.dirname(__file__)


def abs_path(*paths):
    """Get the absolute path of the given file path.

    Args:
        *paths: path parts.

    Returns:
        An abs path string.
    """
    return os.path.abspath(os.path.join(script_dir, '..', *paths))


def read_json(*paths):
    path = abs_path(*paths)
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
            yield obj, key, value
            if not is_basic(value):
                for a, b, c in traverse(value):
                    yield a, b, c
    elif isinstance(obj, list):
        for key, value in enumerate(obj):
            yield obj, key, value
            if not is_basic(value):
                for a, b, c in traverse(value):
                    yield a, b, c

