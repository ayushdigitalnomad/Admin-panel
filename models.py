from django.db import models
from djongo import models

class MongoDBInstance(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    port = models.IntegerField(default=27017)
    # Add other fields as needed
    @property
    def total_users(self):
        total_users = sum(database.users.count() for database in self.databases.all())
        return total_users
class MongoDBDatabase(models.Model):
    instance = models.ForeignKey(MongoDBInstance, on_delete=models.CASCADE,related_name='databases')
    name = models.CharField(max_length=100)

class MongoDBUser(models.Model):
    database = models.ForeignKey(MongoDBDatabase, on_delete=models.CASCADE,related_name='users')
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20,choices=[('edit', 'Edit Access'), ('read', 'Read-only Access')])
class AccessRole(models.Model):
    user = models.ForeignKey(MongoDBUser, on_delete=models.CASCADE, related_name='access_roles')
    database = models.ForeignKey(MongoDBDatabase, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('edit', 'Edit Access'), ('read', 'Read-only Access')])
