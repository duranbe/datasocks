# Generated by Django 3.2.5 on 2022-06-25 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasocks", "0015_auto_20220625_2137"),
    ]

    operations = [
        migrations.AddField(
            model_name="machineaccessapikey",
            name="prefix",
            field=models.CharField(
                default=3, editable=False, max_length=8, unique=True
            ),
            preserve_default=False,
        ),
    ]
