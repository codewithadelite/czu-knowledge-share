"""
Module for views functions decorators
"""

from django.shortcuts import redirect
from django.urls import reverse


def admin_verification(view_func):
    """
    Function to allow only administrators to view their specific pages they are permitted to view
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_admin == True:
            return view_func(request, *args, **kwargs)
        return redirect(reverse('auth_failed'))
    return wrapper

def student_verification(view_func):
    """
    Function to allow only students to view pages they are permitted to view
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_admin == False:
            return view_func(request, *args, **kwargs)
        return redirect(reverse('auth_failed'))
    return wrapper