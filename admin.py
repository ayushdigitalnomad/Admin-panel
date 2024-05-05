from django.contrib import admin
from .models import MongoDBInstance, MongoDBUser,MongoDBDatabase
# Register your models here.
admin.site.register(MongoDBUser)
admin.site.register(MongoDBDatabase)
admin.site.register(MongoDBInstance)
