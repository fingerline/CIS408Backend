from django.db import models

class CSUClass(models.Model):
    cid = models.IntegerField()
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=5, default = "UNK")
    semester = models.CharField(max_length=8, default = "UNK")
    section = models.CharField(max_length=5)
    session = models.CharField(max_length=50)
    begindate = models.DateField(null=True)
    enddate = models.DateField(null=True)
    timestart = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    timeend = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    location = models.CharField(max_length=30)
    instructor = models.CharField(max_length=60)
    classtype = models.CharField(max_length=5)
    openstatus = models.BooleanField()
    enrolled = models.IntegerField()
    capacity = models.IntegerField()
    credits = models.DecimalField(max_digits=2, decimal_places=1)
    consent = models.CharField(max_length=80)
    lastadddate = models.DateField(null=True)
    lastdropdate = models.DateField(null=True)
    lastwithdrawdate = models.DateField(null=True)
    specialtopic = models.CharField(max_length=100, default=None, null=True)
    desc = models.TextField(null=True)

class CSUClassDays(models.Model):
    day = models.CharField(max_length=10)
    classassoc = models.ForeignKey(CSUClass, on_delete=models.CASCADE)

class CSUTags(models.Model):
    tagname = models.CharField(max_length=30)
    tagabbr = models.CharField(max_length=6, default=None, null=True, blank=True)
    classassoc = models.ForeignKey(CSUClass, on_delete=models.CASCADE)