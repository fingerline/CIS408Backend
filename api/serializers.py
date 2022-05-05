from rest_framework import serializers
from api.models import CSUClass, CSUClassDays, CSUTags

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSUTags
        fields = ['tagname', 'tagabbr']

class ClassSerializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField('get_days')
    tags = TagSerializer(source='csutags_set', many=True, read_only=True)
    timestartformat = serializers.TimeField(source = 'timestart', format="%I:%M %p")
    timeendformat = serializers.TimeField(source = 'timeend', format="%I:%M %p")

    def get_days(self, obj):
        return list(CSUClassDays.objects.filter(classassoc__id=obj.id).values_list('day',flat=True))

    def get_tags(self, obj):
        return list(CSUTags.objects.filter(classassoc__id=obj.id))

    class Meta:
        model = CSUClass
        fields = ["cid", "name", "subject", "semester", "section", "session", "begindate", "enddate",
         "days", "timestartformat", "timeendformat", "location", "instructor", "classtype",
          "openstatus", "enrolled", "capacity", "credits", "consent", "lastadddate",
           "lastdropdate", "lastwithdrawdate", "tags"]