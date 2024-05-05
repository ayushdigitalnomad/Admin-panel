# forms.py
from django import forms
from .models import MongoDBInstance,MongoDBUser,AccessRole,MongoDBDatabase
class MongoDBInstanceForm(forms.ModelForm):
    class Meta:
        model = MongoDBInstance
        fields = ['name', 'host', 'port']

class MongoDBUserForm(forms.ModelForm):
    class Meta:
        model = MongoDBUser
        fields = ['username', 'password', 'role']

class AccessRoleForm(forms.ModelForm):
    class Meta:
        model = AccessRole
        fields = ['database', 'role']

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(label='New Password', max_length=100, widget=forms.PasswordInput)

class AssignUserToDatabaseForm(forms.Form):
    user = forms.ModelChoiceField(queryset=MongoDBUser.objects.all())
    database = forms.ModelChoiceField(queryset=MongoDBDatabase.objects.all())

