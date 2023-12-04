from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Department


@login_required
def departments_list(request):
    """
    This function get a list of departments from the database.
    """
    
    context = {'current_page': 'departments_list'}
    departments = Department.objects.all()
    return render(request, 'departments/departments_list.html', {'departments': departments, 'context': context})
