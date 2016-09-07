from django.contrib import admin
from django.conf import settings
from . import models

admin.site.register(models.Post)
admin.site.register(models.PostComment)