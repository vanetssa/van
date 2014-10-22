from django.http import HttpResponse

def index(request):
	return HttpResponse("김상은")

def study(reques):
	return HttpResponse("study page")

def blog(reques):
	return HttpResponse("blog page")

def community(reques):
	return HttpResponse("community page")