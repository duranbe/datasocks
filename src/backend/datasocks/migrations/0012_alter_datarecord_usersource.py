# Generated by Django 3.2.5 on 2022-06-23 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("datasocks", "0011_auto_20220623_1722"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datarecord",
            name="usersource",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="datarecord",
                to="datasocks.machine",
            ),
        ),
    ]
