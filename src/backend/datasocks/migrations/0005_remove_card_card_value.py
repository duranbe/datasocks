# Generated by Django 3.2.5 on 2022-06-12 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasocks', '0004_alter_datarecord_data_json'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='card_value',
        ),
    ]