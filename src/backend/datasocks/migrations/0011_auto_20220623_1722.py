# Generated by Django 3.2.5 on 2022-06-23 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("datasocks", "0010_machineaccess_machineaccessapikey"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MachineAccess",
            new_name="Machine",
        ),
        migrations.AlterModelOptions(
            name="machineaccessapikey",
            options={"verbose_name": "Machine Access API Key"},
        ),
    ]
