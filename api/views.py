from django.shortcuts import render

# Create your views here.
from .models import Task
from django.core import serializers
from django.http import HttpResponse
import json


def index(request):
    #task_list = serializers.serialize('python', Task.objects.all())
    task_list = Task.objects.filter(status__exact=1)
    to_return = []

    for item in task_list:
        to_return.append(prepare_item(item))

    return HttpResponse(json.dumps(to_return, default=str))


def update(request):
    if request.method == 'POST':
        params = json.loads(request.body.decode('utf-8'))

        for param in params:
            model = Task.objects.get(pk=param['id'])
            model.name = param['title']
            model.is_completed = int (param['completed'])
            if 'status' in param:
                model.status = param['status']
            model.save()

        return HttpResponse([{'code': 200, 'message': 'OK'}])

    return HttpResponse([{'code': 500, 'message': 'Request is not an AJAX or POST or no data found'}])


def prepare_item(object):
    return {'id': object.pk, 'title': object.name, 'completed': object.is_completed, 'created_at': object.created_at}



