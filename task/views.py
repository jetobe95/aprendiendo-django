from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
  task = forms.CharField(label="New task")
# Create your views here.
def index(request):
  if "tasks" not in request.session:
    request.session["tasks"] = []
  return render(request,"tasks/index.html",{
    'tasks': request.session["tasks"],
  })

def add(req):
  if req.method == "POST":
    form = NewTaskForm(req.POST)
    if form.is_valid():
      task = form.cleaned_data['task']
      req.session["tasks"]+=[task]
      return HttpResponseRedirect(reverse('tasks:index'))
    else:
       return render(req,"tasks/add.html",{
    'form':form
  })

  return render(req,"tasks/add.html",{
    'form':NewTaskForm()
  })