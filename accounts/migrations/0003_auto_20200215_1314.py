# Generated by Django 3.0.3 on 2020-02-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200215_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='skills',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.TextField(default=''),
        ),
    ]
