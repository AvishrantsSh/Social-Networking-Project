from django.contrib import admin

from backend.models import Messages, Posts, Session, Users

admin.site.register(Users)
admin.site.register(Session)
admin.site.register(Messages)
admin.site.register(Posts)
# Register your models here.
