from http.client import HTTPResponse
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from api.models import CSUClass
from api.serializers import ClassSerializer


def class_list(request):
    if request.method == 'GET':
        classes = CSUClass.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return JsonResponse(serializer.data, safe=False)

def class_detail(request, id):
    try:
        course = CSUClass.objects.get(id=id)
    except CSUClass.DoesNotExist:
        return HttpResponse("Can't find that!")
    serializer = ClassSerializer(course)
    return JsonResponse(serializer.data)