from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.Index),
    path('post/<slug:slug>', views.Detail, name="post-detail")
]
