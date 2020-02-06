'''Utilities for web APIs'''
from datetime import datetime, date
import json
import numpy as np

from flask import jsonify, request

class CustomJSONEncoder(json.JSONEncoder):
    '''Custom JSON encoder for use in API and database'''

    def default(self, obj):
        # convert dates and numpy objects in a json serializable format
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif type(obj) in (np.int_, np.intc, np.intp, np.int8, np.int16,
                           np.int32, np.int64, np.uint8, np.uint16,
                           np.uint32, np.uint64):
            return int(obj)
        elif type(obj) in (np.bool_,):
            return bool(obj)
        elif type(obj) in (np.float_, np.float16, np.float32, np.float64,
                           np.complex_, np.complex64, np.complex128):
            return float(obj)

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

def custom_json_encoder(obj):
    return json.dumps(obj, cls=CustomJSONEncoder)

def custom_json_decoder(json_string):
    dct = json.loads(json_string, object_hook=datetime_parser)
    return dct