# Generated by Django 2.2.4 on 2020-02-15 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('decription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='events/')),
                ('address', models.CharField(blank=True, max_length=80, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('skills', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='profiles.Skills')),
            ],
        ),
    ]