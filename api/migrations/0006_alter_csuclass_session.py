# Generated by Django 4.0.4 on 2022-04-27 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_csuclass_begindate_alter_csuclass_enddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csuclass',
            name='session',
            field=models.CharField(max_length=50),
        ),
    ]