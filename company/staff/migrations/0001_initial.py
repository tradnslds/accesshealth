# Generated by Django 3.2.2 on 2021-05-11 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_name', models.CharField(max_length=30)),
                ('Manager', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_name', models.CharField(max_length=30)),
                ('Department', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Picture', models.CharField(max_length=128)),
            ],
        ),
    ]
