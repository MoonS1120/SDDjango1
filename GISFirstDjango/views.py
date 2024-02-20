from django.shortcuts import render
from .models import Person

def splash(request):
    name = 'Billy'
    subject_list = ['Chemistry', 'Mathematics', 'Economics']
    people = Person.objects.all()
    debug_people = list(people)
    return render(request, "splash.html", {'name': name, 'subject_list': subject_list, 'people': debug_people})