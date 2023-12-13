from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import TodoListForm
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

# def update_model_name(request, id):
#   model_instance = ModelName.objects.get(id=id)
#   if request.method == "POST":
#     form = ModelForm(request.POST, instance=model_instance)
#     if form.is_valid():
#       # To redirect to the detail view of the model, use this:
#       model_instance = form.save()
#       return redirect("detail_url", id=model_instance.id)

    #   To add something to the model, like setting a user,
    #   use something like this:
    #   
    #   model_instance = form.save(commit=False)
    #   model_instance.user = request.user
    #   model_instance.save()
    #   return redirect("detail_url", id=model_instance.id)
#   else:
#     form = ModelForm(instance=model_instance)

#   context = {
#     "form": form
#   }

#   return render(request, "model_names/edit.html", context)
