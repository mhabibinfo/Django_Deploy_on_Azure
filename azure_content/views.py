from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import *
def test(request):
    return HttpResponse("<h1>Hellow this is my first deployment done!</h1>")

def testing(request):
    return HttpResponse("<h1>I have make some changes in this great project</h1>")

def index(request):
    return HttpResponse("<h1>This is index page! with update changes</h1>")

class HomeView(ListView):
    context_object_name = 'project_list'
    model = Project
    template_name = "azure_content/home.html"

class AboutView(TemplateView):
    template_name = "azure_content/about.html"

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description']
    template_name = "azure_content/create.html"
    success_url ="/"

class ProjectEditView(UpdateView):
    model = Project
    fields = ['name','description']
    template_name = "azure_content/create.html"
    success_url ="/"

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "azure_content/delete.html"
    fields = ['name']
    success_url ="/"

