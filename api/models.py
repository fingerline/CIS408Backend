from django.db import models

class CSUClass(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    section = models.IntegerField()
    session = models.CharField(max_length=30)
    begindate = models.DateField()
    enddate = models.DateField()
    timestart = models.TimeField(auto_now=False, auto_now_add=False)
    timeend = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=30)
    instructor = models.CharField(max_length=60)
    classtype = models.CharField(max_length=5)
    openstatus = models.BooleanField()
    enrolled = models.IntegerField()
    capacity = models.IntegerField()
    credits = models.DecimalField(max_digits=2, decimal_places=1)
    consent = models.CharField(max_length=80)
    lastadddate = models.DateField()
    lastdropdate = models.DateField()
    lastwithdrawdate = models.DateField()

class CSUClassDays(models.Model):
    day = models.CharField(max_length=10)
    classassoc = models.ForeignKey(CSUClass, on_delete=models.CASCADE)

class CSUTags(models.Model):
    tagname = models.CharField(max_length=30)
    tagabbr = models.CharField(max_length=6, default=None, null=True, blank=True)
    classassoc = models.ForeignKey(CSUClass, on_delete=models.CASCADE)