# Generated by Django 4.0 on 2022-01-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_guide',
            fields=[
                ('guide_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('guide_name', models.CharField(max_length=200)),
                ('guide_email', models.CharField(max_length=100)),
                ('guide_address', models.CharField(max_length=100)),
                ('guide_phone', models.CharField(max_length=10)),
                ('guide_descripition', models.CharField(max_length=500)),
                ('guide_image', models.FileField(upload_to='guide_images')),
            ],
            options={
                'db_table': 'book_guide',
            },
        ),
    ]