from django.shortcuts import render, get_object_or_404
from todos.models import TodoList
# Create your views here.

def todo_list(request):
    list = TodoList.objects.all()
    context = {
    "todo_list_list": list,
    }
    return render(request, "todos/todo_list.html", context)

# 1st: Create a view that shows the details of a particular to-do list, including its tasks
def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    tasks = todo_list.items.all()
    context = {
        "todo_list": todo_list,
        "tasks": tasks,
    }

    return render(request, "todos/detail.html", context)
