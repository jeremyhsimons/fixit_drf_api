# Generated by Django 3.2.20 on 2023-09-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Title', max_length=200),
        ),
    ]