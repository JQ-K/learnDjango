# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models
# Create your views here.

def cart(request):
	uid = request.session['user_id']
	context = {}
	return render(request,'',context)
