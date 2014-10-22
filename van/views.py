# -*- coding: utf-8 -*-
from django.http import HttpResponse

def index(request):
	return HttpResponse("장도우와 황서정은 나쁩니다.")

def study(reques):
	return HttpResponse("study page")

def blog(reques):
	return HttpResponse("blog page")

def community(reques):
	return HttpResponse("community page")