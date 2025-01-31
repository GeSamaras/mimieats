from django.db import models
# this file works as an ORM, where classes become
# database tables. classes are the columns, and 
# instances are the rows for that data table. 



# these models all have their basic fields to be
# filled up when entering a new database entry
# each with their types preceded by models.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField() # TextField() makes so body holds a dynamic string length 
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

# Create your models here.
