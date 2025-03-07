from django.urls import path
from . import views

urlpatterns = [
    path("general/", view=views.general, name="general"),
]
