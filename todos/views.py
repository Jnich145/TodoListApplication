from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm
from todos.forms import TodoItemForm
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

def todo_list_create(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form = form.save() # these embedded lines reference the Model
            return redirect("todo_list_detail", id=form.id)
    else:
        form = TodoListForm()

    context = {
        "form": form,
    }

    return render(request, "todos/create.html", context)

def todo_list_update(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form = form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=todo_list)

    context = {
        "todo_list_object": todo_list,
        "edit_form": form,
    }
    return render(request, "todos/edit.html", context)

def todo_list_delete(request, id):
    todo_list = TodoList.objects.get(id=id)
    if request.method == "POST":
        todo_list.delete()
        return redirect("todo_list_list")

    return render(request, "todos/delete.html")

def todo_item_create(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm()

    context = {
        "create_form": form,
    }

    return render(request, "todos/create_item.html", context)
