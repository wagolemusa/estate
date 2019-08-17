from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import (
	home,
	post_create,
	post_detail,
	post_update,
	post_delete,

	)

urlpatterns = [
    path('', home, name='home'),
    path('create', post_create),
    path('detail', post_detail),
    path('update', post_update),
    path('delete', post_delete),
]
