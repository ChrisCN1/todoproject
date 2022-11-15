from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Tasks



@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def create_item(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        new_task = Tasks(title=body['title'], description=body['description'], due_date=body['due date'])
        new_task.save()
    return render(request, 'index.html')

@csrf_exempt
def todo_page(request, id):
    all_tasks = Tasks.objects.all()
    data = {'url_id': id, 'all_tasks': all_tasks}
    return render(request, 'task_details.html', data)

@csrf_exempt
def display_list(request):
    all_tasks = Tasks.objects.all()
    return render(request, 'displaylist.html', {'all_tasks': all_tasks})

@csrf_exempt
def edit_list(request):
    return 

@csrf_exempt
def delete_task(request):
    pass