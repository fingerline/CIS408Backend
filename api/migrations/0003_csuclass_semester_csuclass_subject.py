# Generated by Django 4.0.4 on 2022-04-27 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_csuclass_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='csuclass',
            name='semester',
            field=models.CharField(default='UNK', max_length=8),
        ),
        migrations.AddField(
            model_name='csuclass',
            name='subject',
            field=models.CharField(default='UNK', max_length=5),
        ),
    ]
