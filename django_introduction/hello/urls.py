from django.urls import path
from . import views

app_name = "hello"

urlpatterns = [
    path("", views.index, name="index"),
    path("goodbye", views.goodbye, name="goodbye"),
    path("<int:num>", views.numero, name="numero"),
    path("<str:name>", views.greet, name="greet")
]