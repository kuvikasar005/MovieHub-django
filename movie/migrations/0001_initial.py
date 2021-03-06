# Generated by Django 3.0.3 on 2020-03-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('cast', models.TextField()),
                ('trailer', models.CharField(max_length=256)),
                ('img', models.ImageField(upload_to='movie_images')),
                ('thumbnail_img', models.ImageField(upload_to='movie_images')),
            ],
        ),
    ]
