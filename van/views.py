from django.http import HttpResponse

def index(request):
	return HttpResponse("hello world!!")

def study(reques):
	return HttpResponse("study page")

def blog(reques):
	return HttpResponse("blog page")

def community(reques):
	return HttpResponse("community page")