# Generated by Django 3.2.5 on 2022-06-14 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasocks', '0006_auto_20220612_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_data_serie', models.CharField(max_length=50, verbose_name='first_data_series')),
                ('second_data_serie', models.CharField(blank=True, max_length=50, null=True, verbose_name='second_data_serie')),
                ('graph_color', models.CharField(default='#f0a860', max_length=7, verbose_name='line_color')),
                ('graph_name', models.CharField(max_length=50, verbose_name='Graph Name')),
                ('graph_type', models.CharField(choices=[('LN', 'Line Plot'), ('AR', 'Area Chart'), ('BR', 'Bar Plot'), ('RD', 'Radar Plot'), ('PI', 'Pie Plot'), ('BL', 'Bubble Plot'), ('ST', 'Scatter Plot')], default=None, max_length=2)),
                ('linked_dshbd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasocks.dashboard')),
            ],
        ),
    ]