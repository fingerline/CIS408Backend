from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from api.models import CSUClass, CSUTags
from api.serializers import ClassSerializer
from datetime import datetime

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
    if 'begintime' in rectdict:
        filters['timestart__gte'] = datetime.strptime(rectdict['begintime'], "%H:%M").time()
    if 'endtime' in rectdict:
        filters['timeend__lte'] = datetime.strptime(rectdict['endtime'], "%H:%M").time()
    if 'tag' in rectdict:
        with_valid_tags = CSUClass.objects.filter(id__in=CSUTags.objects.filter(tagabbr=rectdict['tag']).values('classassoc'))

    output = with_valid_tags.filter(**filters)
    serializer = ClassSerializer(output, many=True)
    if len(serializer.data) == 0:
        return HttpResponse("No Classes Found")
    return JsonResponse(serializer.data, safe=False)

