# -*- coding: utf-8 -*-

# Disable doc-string warning for test files
# pylint: disable=C0111

import json


class ZipkinEndPointModel(object):

    def __init__(self):
        self.serviceName = ""
        self.ipv4 = "localhost"


class ZipkinSpanModel(object):

    def __init__(self):
        self.traceId = ""
        self.parentId = ""
        self.id = ""
        self.kind = "SERVER"
        self.name = ""
        self.timestamp = 0
        self.duration = 0
        self.localEndpoint = {}
        self.shared = True


class ZipkinTracer(object):
    """
    Class to generate ZipKin Trace logs .
    """
    def __init__(self, save_path):
        self.save_path = save_path
        self.spans = []

    def add_span(self, span):
        self.spans.append(span)

    def save_trace(self):
        with open(self.save_path, 'a') as tracefile:
            json_dump = json.dumps(self.spans,
                                   default=lambda o: o.__dict__,
                                   indent=4, cls=ComplexEncoder)
            tracefile.write(json_dump)


class ComplexEncoder(json.JSONEncoder):

    def default(self, z):
        if isinstance(z, ZipkinEndPointModel):
            return z.toJson
        else:
            return super(ComplexEncoder, self).default(z)
