from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
	return HttpResponse("<h1>List Home</h1>")
	
def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request):
	return HttpResponse("<h1>Show page</h1>")

def post_list(request):
	return HttpResponse("<h1>List</h1>")

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")



