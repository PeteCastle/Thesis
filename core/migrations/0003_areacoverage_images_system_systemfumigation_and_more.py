# Generated by Django 5.0.3 on 2024-03-29 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_mosquitosystem_secret_key_alter_mosquitoimages_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCoverage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='mosquitoes')),
                ('area_latitude', models.FloatField()),
                ('area_longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='mosquitoes')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('detected_mosquito_count', models.IntegerField()),
                ('prediction_time', models.FloatField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.areacoverage')),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('secret_key', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='mosquitoes')),
                ('location_name', models.CharField(max_length=100)),
                ('location_latitude', models.FloatField()),
                ('location_longitude', models.FloatField()),
                ('location_radius', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SystemFumigation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fumigation_date', models.DateTimeField()),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.system')),
            ],
        ),
        migrations.CreateModel(
            name='SystemStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.system')),
            ],
        ),
        migrations.CreateModel(
            name='SystemWaterLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('water_level', models.FloatField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.system')),
            ],
        ),
        migrations.DeleteModel(
            name='MosquitoImages',
        ),
        migrations.DeleteModel(
            name='MosquitoSystem',
        ),
        migrations.AddField(
            model_name='images',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.system'),
        ),
    ]
