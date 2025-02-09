from django.db import models
# this file works as an ORM, where classes become
# database tables. classes are the columns, and 
# instances are the rows for that data table. 
# using SQLite by default, however firebase will be used. 

# https://realpython.com/django-migrations-a-primer/
# in order to update the ORM with new tables, run:
# python manage.py makemigrations, while inside the project with (venv)

# after makemigrations, to save them we need to run:
# python manage.py migrate


# these models all have their basic fields to be
# filled up when entering a new database entry
# each with their types preceded by models.

""" class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
 """

class Category(models.Model):
    name = models.CharField(max_length=30)

    # this will override the model name in admin's dashboard
    # for better readability
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField() # TextField() makes so body holds a dynamic string length 
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.ManyToManyField
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title



class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # ForeignKey() is also similar to ManyToManyField
    # since many posts can be made by the same one user
    # this method defines a Many-to-one relationship where
    # the user is the owner of many post models. 
    # two parameters, the relationship, and what django does
    # once the post is deleted. It will remove all child posts
    # to that specific post. 
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    # these dunder str functions serve to better represent
    # the models, by return a formatted version of their
    # fields, names, contents and such
    def __str__(self):
        return f"{self.author} on '{self.post}'"