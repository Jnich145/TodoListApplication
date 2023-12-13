from django.urls import path
from todos.views import todo_list, todo_list_detail, todo_list_create

urlpatterns = [
    path("", todo_list, name="todo_list_list"),
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("create/", todo_list_create, name="todo_list_create")
]

# 2nd: In the todos urls.py file, register the view with the path "<int:id>/" and the name "todo_list_detail"