# Generated by Django 4.0.4 on 2022-04-28 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_csuclass_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='csuclass',
            name='cid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='csuclass',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]