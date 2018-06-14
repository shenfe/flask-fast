from flask_restplus import fields
from .helper import Mod as Model


TimeRange = Model('TimeRange', {
    'start': fields.DateTime(description='start time'),
    'end': fields.DateTime(description='end time')
})
