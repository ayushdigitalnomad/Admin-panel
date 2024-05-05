from django.shortcuts import render
from .models import MongoDBInstance, MongoDBDatabase, MongoDBUser
from django.shortcuts import render, redirect,get_object_or_404
from .models import MongoDBUser, AccessRole
from .forms import MongoDBUserForm, AccessRoleForm, ChangePasswordForm,AssignUserToDatabaseForm
from django.contrib.auth.decorators import login_required

def index(request):
    mongodb_instances = MongoDBInstance.objects.all()
    mongodb_databases = MongoDBDatabase.objects.all()
    mongodb_users = MongoDBUser.objects.all()
    return render(request, 'index.html', {'mongodb_instances': mongodb_instances, 'mongodb_databases': mongodb_databases, 'mongodb_users': mongodb_users})
#MongoDB Instance Management
def add_instance(request):
    if request.method == 'POST':
        # Process form data and create new MongoDB instance
        ...
    return render(request, 'add_instance.html')

def list_instances(request):
    instances = MongoDBInstance.objects.all()
    return render(request, 'list_instances.html', {'instances': instances})

def create_user(request):
    if request.method == 'POST':
        form = MongoDBUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = MongoDBUserForm()
    return render(request, 'create_user.html', {'form': form})

def list_users(request):
    users = MongoDBUser.objects.all()
    return render(request, 'list_users.html', {'users': users})

"""def change_password(request, user_id):
    user = MongoDBUser.objects.get(id=user_id)
    if request.method == 'POST':
        # Process form data and change user password
        ...
        return redirect('list_users')
    return render(request, 'change_password.html', {'user': user})"""
def change_password(request, user_id):
    user = get_object_or_404(MongoDBUser, id=user_id)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user.password = new_password
            user.save()
            return redirect('list_users')
    else:
        form = ChangePasswordForm()
    return render(request, 'change_password.html', {'form': form, 'user': user})


"""def remove_user(request, user_id):
    user = MongoDBUser.objects.get(id=user_id)
    user.delete()
    return redirect('list_users')"""
# views.py
def remove_user(request, user_id):
    user = get_object_or_404(MongoDBUser, id=user_id)
    user.delete()
    return redirect('list_users')

# views.py
def remove_database(request, database_id):
    database = get_object_or_404(MongoDBDatabase, id=database_id)
    database.delete()
    return redirect('list_databases')

def assign_role(request):
    if request.method == 'POST':
        form = AccessRoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = AccessRoleForm()
    return render(request, 'assign_role.html', {'form': form})

@login_required
def restricted_view(request):
    # Check user role or any other criteria
    user = request.user
    if user.is_superuser:
        # Admin has unrestricted access
        return render(request, 'restricted_view.html')
    else:
        # Apply custom authentication restrictions
        # For example, restrict access based on user role
        if user.role == 'admin':
            return render(request, 'restricted_view.html')
        else:
            return render(request, 'access_denied.html')

def remove_user_access(request, user_id, database_id):
    user = get_object_or_404(MongoDBUser, id=user_id)
    database = get_object_or_404(MongoDBDatabase, id=database_id)
    user.access_roles.filter(database=database).delete()
    return redirect('list_users')


def assign_user_to_database(request):
    if request.method == 'POST':
        form = AssignUserToDatabaseForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user']
            database_id = form.cleaned_data['database']
            user = get_object_or_404(MongoDBUser, id=user_id)
            database = get_object_or_404(MongoDBDatabase, id=database_id)
            # Create access role for the user and database
            access_role = AccessRole.objects.create(user=user, database=database, role='edit')
            access_role.save()
            return redirect('list_users')
    else:
        form = AssignUserToDatabaseForm()
    return render(request, 'assign_user_to_database.html', {'form': form})
