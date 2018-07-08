#!/usr/bin/env python
# coding=utf-8

from django.http import HttpResponse

class MyException(object):
    def process_exception(request, response, exception):
        return HttpResponse(exception.message)
