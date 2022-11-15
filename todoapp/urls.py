from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('todos/new', views.create_item, name="create item"), #create todo
    path('todos/<int:id>', views.todo_page, name="find item"), #find todo
    path('todos', views.display_list, name="display list"), #show all items
    path('todos/<int:id>/edit', views.edit_list, name="edit item"), #update items
    path('todos/<int:id>/delete', views.delete_task, name="delete item") #delete todo
]
