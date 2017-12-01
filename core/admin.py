from django.contrib import admin
from django.contrib.auth.models import User
from .models import Task, Comment, Team, Notification, Mail

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(Team)
admin.site.register(Mail)

