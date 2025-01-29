from django.contrib import admin

# Register your models here.
from .models import user, tips,room, message,topic, update
admin.site.register(user)
admin.site.register(tips)
admin.site.register(room)
admin.site.register(message)
admin.site.register(topic)
admin.site.register(update)




