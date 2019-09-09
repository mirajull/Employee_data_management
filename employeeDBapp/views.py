from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import loader

#from employeeSite import employeeDBapp
from django.views.generic import CreateView
from .models import Person

class PersonCreateView(CreateView):
     model = Person
     fields = ('name', 'email', 'job_title', 'bio')


# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return render(request, 'base.html', {'message': 'Hello', 'PageTitle': 'Hello'})
