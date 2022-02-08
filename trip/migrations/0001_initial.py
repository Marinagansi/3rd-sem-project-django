# Generated by Django 4.0 on 2022-02-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TripPackage',
            fields=[
                ('package_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('package_name', models.CharField(max_length=100)),
                ('trip_days', models.CharField(max_length=100)),
                ('itinary_route', models.CharField(max_length=150)),
                ('details1', models.CharField(max_length=200)),
                ('details2', models.CharField(max_length=200)),
                ('trip_image', models.FileField(upload_to='trip')),
            ],
            options={
                'db_table': 'trip',
            },
        ),
    ]