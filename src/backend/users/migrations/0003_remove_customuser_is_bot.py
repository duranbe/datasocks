# Generated by Django 3.2.5 on 2022-06-20 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_is_bot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_bot',
        ),
    ]
