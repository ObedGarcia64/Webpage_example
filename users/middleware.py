""" Complete profile middleware """

from django.http import response
from django.shortcuts import render, redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """ Profile completion middleware
    ensure every user is interacting with the platform
    have their profile"""

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_staff and not request.user.is_anonymous:

            try:
                profile = request.user.teacher
            except:
                pass
            try:
                profile = request.user.student
            except:
                pass

            if profile.type_of_user == "teacher" :
                if not profile.title:
                    if request.path not in [reverse('update_teacher_profile'), reverse('logout')]:
                        return redirect('update_teacher_profile')
            elif profile.type_of_user == "student":
                if not profile.type_of_user == 'student':
                    if not profile.student_number or profile.subject or profile.group or profile.career:
                        if request.path not in [reverse('update_student_profile'), reverse('logout')]:
                            return redirect('update_student_profile')
                
        response = self.get_response(request)
        return response