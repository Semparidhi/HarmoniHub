from django.contrib import admin
from .models import Song
from .models import Singer
from .models import album
from .models import podcast

# Register your models here.
admin.site.register(Song)
admin.site.register(Singer)
admin.site.register(album)
admin.site.register(podcast)