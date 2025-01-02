from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki_entry, name="wiki_entry"),
    path("create_page", views.create_page, name="create_page"),
    path("random_entry", views.random_entry, name="random_entry"),
    path("edit/<str:title>", views.edit_entry, name="edit_entry"),
    path("search", views.search_entry, name="search_entry")
]