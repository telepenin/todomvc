import json

from django.http import HttpResponse

from .models import Task


def index(request):
    task_list = Task.objects.filter(status__exact=1)
    to_return = []

    # FIXME: you can try to find return queryset as a dict
    # instead process explicitly
    for item in task_list:
        to_return.append(prepare_item(item))

    return HttpResponse(json.dumps(to_return, default=str))


def update(request):
    if request.method == 'POST':
        # FIXME: possible EncodeDecodeError
        params = json.loads(request.body.decode('utf-8'))

        for param in params:
            # FIXME: query in the loop
            model = Task.objects.get(pk=param['id'])

            model.name = param['title']

            # FIXME: "Completed" bool or int? unclear
            model.is_completed = int(param['completed'])
            if 'status' in param:
                model.status = param['status']
            model.save()

        return HttpResponse([{'code': 200, 'message': 'OK'}])

    return HttpResponse([{'code': 500,
                          'message': 'Request is not an AJAX or '
                                     'POST or no data found'}])


def prepare_item(object):
    return {'id': object.pk,
            'title': object.name,
            'completed': object.is_completed,
            'created_at': object.created_at}
