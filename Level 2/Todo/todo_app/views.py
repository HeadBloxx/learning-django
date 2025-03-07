from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

error_message = ""
def index(request):
    global error_message
    err = error_message
    if request.method == "POST":
        raw = request.POST.get("action", "")
        action = request.POST.get("action", "").split("-")
        if action[0] == "add":
            user_text = request.POST.get("task_text", "").strip()
            
            if not user_text:
                error_message = "Input cannot be empty!"
            elif len(user_text) < 3:
                error_message = "Input must be at least 3 characters long."
            else: # all good
                Task(text=user_text, priority=1).save()
                error_message = ""
            #return redirect("index")
        elif action[0] == "complete" or action[0] == "delete":
            try:
                Task.objects.get(id=int(action[1])).delete()
            except:
                print("no id")
            #return redirect("index")
        

    tasks = Task.objects.all()
    return render(request, "todo_app/index.html", {"tasks": tasks, "error_message": err})
