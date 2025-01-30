from django.shortcuts import render
from firebase_admin import firestore

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
