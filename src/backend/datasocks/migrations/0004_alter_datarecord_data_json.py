# Generated by Django 3.2.5 on 2022-06-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasocks', '0003_auto_20220612_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarecord',
            name='data_json',
            field=models.JSONField(),
        ),
    ]
