from django.urls import path
from . import views

# Routes are the URL's for pages and post in the
# project, which get contructed with patterns for
# each unique post. Once they're created inside
# the project codebase, they must be added to the
# configuration /mimieats/urls.py  

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
]