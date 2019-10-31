# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Todo
from .serializers import TodoSerializer

@csrf_exempt
def todo_list(request):

    if request.method == 'GET':
        todo_list = Todo.objects.all()
        serializer = TodoSerializer(todo_list, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)

@csrf_exempt
def todo_detail(request, pk):

    try:
        todo_item = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodoSerializer(todo_item)

        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(todo_item, data=data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        todo_item.delete()

        return HttpResponse(status=204)
