# Generated by Django 3.2.5 on 2022-06-20 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasocks', '0008_graph_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='linked_dshbd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graph', to='datasocks.dashboard'),
        ),
    ]
