# Generated by Django 3.0.3 on 2020-02-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('school', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('clubs', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=200)),
                ('why_aims', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=-1)),
            ],
        ),
    ]
