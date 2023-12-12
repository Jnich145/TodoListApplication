from django.shortcuts import render
from todos.models import TodoList
# Create your views here.

def todo_list(request):
    list = TodoList.objects.all()
    context = {
    "todo_list_list": list,
    }
    return render(request, "todos/todo_list.html", context)
