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
app_name = 'estate'
urlpatterns = [
    path('', home, name='home'),
    path('create', post_create),
    path('<int:id>/', post_detail, name="detail"),
    path('<int:id>/edit/', post_update, name="update"),
    path('delete', post_delete),
]
