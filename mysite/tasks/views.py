from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# python manage.py migrate --> allows tables to be created
#tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    if "tasks" not in request.session:  # is there any "tasks" inside of the session
        request.session["tasks"] = []   # if not, give a tasks

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST) # user's submitted data 
        if form.is_valid():
            task = form.cleaned_data["task"] #all data user submitted
            request.session["tasks"] += [task] #adds the task comes from user post to the session's tasks
            return HttpResponseRedirect(reverse("tasks:index")) # reverse -> finds url of tasks:index
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })