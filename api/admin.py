from django.contrib import admin
from .models import User, Photo, Comment, Like

admin.site.register(User)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Like)
