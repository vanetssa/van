from django.http import HttpResponse
import os

def index(request):
	return HttpResponse("hello world!!")

def pull(request):
	os.system('cd /website/van && sudo -u van git reset --hard HEAD && sudo -u van git pull origin mas')
	return HttpResponse("")
