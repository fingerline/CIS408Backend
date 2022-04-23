from rest_framework import serializers
from api.models import CSUClass, CSUClassDays, CSUTags

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSUTags
        fields = ['tagname', 'tagabbr']

class ClassSerializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField('get_days')
    tags = TagSerializer(source='csutags_set', many=True, read_only=True)

    def get_days(self, obj):
        return list(CSUClassDays.objects.filter(classassoc__id=obj.id).values_list('day',flat=True))

    def get_tags(self, obj):
        return list(CSUTags.objects.filter(classassoc__id=obj.id))

    class Meta:
        model = CSUClass
        fields = ["id", "name", "section", "session", "begindate", "enddate",
         "days", "timestart", "timeend", "location", "instructor", "classtype",
          "openstatus", "enrolled", "capacity", "credits", "consent", "lastadddate",
           "lastdropdate", "lastwithdrawdate", "tags"]