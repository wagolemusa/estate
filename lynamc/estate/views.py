from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Post
from .forms import PostForm
# Create your views here.


def home(request):
	queryset = Post.objects.all()

	context =	{
		"query_list": queryset,
		"title": "List"
	}
	# return HttpResponse("<h1>List Home</h1>")
	return render(request, "index.html", context)

def post_create(request):
	form  = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messege success
		messages.success(request, "<a href='#'>itme</a> successfuly Created", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_obsolute_url())
	else:
		messages.error(request, "Not successful Created")

	context = {
		"form": form,
	}
	return render(request, "post_forms.html", context)


def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"instance" : instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	return HttpResponse("<h1>List</h1>")

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messege success
		messages.success(request, "Succesfuly Updated")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Updated")
	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_update.html", context)

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")



