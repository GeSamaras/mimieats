from django.contrib import admin
# import all models to be registered
from blog.models import Category, Comment, Post

# Register your models here.

# https://realpython.com/django-user-management/
# createsuperuser
# the way to give devs admin access to the project
# creating, updating and deleting model classes from
# a web gui
# http://localhost:8000/admin

# models from models.py also need to be registered in
# admin.py, each model points to an admin class. 


# defaults for now, but these classes can be coded
# so they change in the admin page for visualization
# and so on
class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)