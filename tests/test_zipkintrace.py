# -*- coding: utf-8 -*-

# Disable doc-string warning for test files
# pylint: disable=C0111

import unittest
import uuid
import tempfile
import os
import shutil

import json

from tests.context import zipkintrace as z

class ZipkinTraceTestSuite(unittest.TestCase):

    @staticmethod
    def _tmp_file():
        temp_directory = tempfile.mkdtemp()
        return os.path.join(temp_directory, "tracefile.json")

    @staticmethod
    def _dummy_span():
        # Create end point
        local_endpoint = z.ZipkinEndPointModel()
        local_endpoint.serviceName = "UnitTest_ServiceName"
        local_endpoint.ipv4 = "ipFromUnitTest"

        # Create Span
        span = z.ZipkinSpanModel()
        span.traceId = "800a8f9572bc21d5"
        span.parentId = ""  #"e35f754e79100a60"
        span.id = uuid.uuid4().hex
        span.name = ""
        span.timestamp = 1564571618000975
        span.duration = 3000000
        span.localEndpoint = local_endpoint

        return span

    def test_add_spans(self):
        # Arrange
        tmp_file = self._tmp_file()
        ztracer = z.ZipkinTracer(tmp_file)
        span = self._dummy_span()

        # Action
        ztracer.add_span(span)
        ztracer.add_span(span)

        # Assert
        self.assertEqual(len(ztracer.spans), 2)
        self.assertEqual(ztracer.spans[0].traceId, "800a8f9572bc21d5")
        #self.assertEqual(ztracer.spans[0].id, "d")

    def test_save_trace_file(self):
        # Arrange
        tmp_file = self._tmp_file()
        print(tmp_file)

        ztracer = z.ZipkinTracer(tmp_file)
        span = self._dummy_span()

        ztracer.add_span(span)
        ztracer.add_span(span)

        # Action
        ztracer.save_trace()

        data = ""
        with open(tmp_file) as json_file:
            data = json.load(json_file)

        print(data)
        # Assert
        self.assertEqual(data[0]["traceId"], "800a8f9572bc21d5")
        self.assertEqual(data[0]["localEndpoint"]["serviceName"], "UnitTest_ServiceName")

        #Cleanup
        self.remove_dir(os.path.dirname(tmp_file))

    def remove_dir(self, path):
        """ param <path> could either be relative or absolute. """
        if os.path.isfile(path):
            os.remove(path)  # remove the file
        elif os.path.isdir(path):
            shutil.rmtree(path)  # remove dir and all contains
        else:
            raise ValueError("file {} is not a file or dir.".format(path))
