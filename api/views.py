from urllib import request
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from api import serializers
from api.models import CSUClass, CSUTags
from api.serializers import ClassSerializer
from rest_framework import generics

def querydict_to_dict(query_dict):
    data = {}
    for key in query_dict.keys():
        v = query_dict.getlist(key)
        if len(v) == 1:
            v = v[0]
        data[key] = v
    return data

def ClassList(request):
    rectdict = querydict_to_dict(request.GET)
    with_valid_tags = CSUClass.objects.all()
    filters = {}
    if 'semester' in rectdict:
        filters['semester'] = rectdict['semester']
    if 'subject' in rectdict:
        filters['subject'] = rectdict['subject'].upper()
    if 'name' in rectdict:
        filters['name__icontains'] = rectdict['name']
    if 'tag' in rectdict:
        with_valid_tags = CSUClass.objects.filter(id__in=CSUTags.objects.filter(tagabbr="TE").values('classassoc'))

    output = with_valid_tags.filter(**filters)
    serializer = ClassSerializer(output, many=True)
    return JsonResponse(serializer.data, safe=False)

