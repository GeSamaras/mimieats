# https://docs.djangoproject.com/en/5.1/topics/templates/

# views.py is a collection of funcs and classes that points to
# different directories in the app. these functions have the
# logic to direct to the pertaining URL.

from django.shortcuts import render
from firebase_admin import firestore
from blog.models import Post, Comment


db = firestore.client()

def save_article(title, content):
    data = {
        "title": title,
        "content": content
    }
    db.collection("articles").add(data)

def index(request):
    articles_ref = db.collection("articles")
    articles = [doc.to_dict() for doc in articles_ref.stream()]
    return render(request, "blog/index.html", {"articles": articles})
# Create your views here.

def blog_index(request):
    # SQL-like python code "FROM Post * ORDER_BY "created_on" "
    # the syntax of the Queryset is: Object.query1().query2("param")
    posts = Post.objects.all().order_by("-created_on") # - for descending order
    
    context = {
        "posts": posts,
    }

    # render method forms a new html from the request input
    # using the context from the dictionary above 
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)