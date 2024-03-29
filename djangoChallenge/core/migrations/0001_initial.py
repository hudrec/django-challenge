# Generated by Django 4.1.7 on 2023-04-26 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('slug', models.CharField(max_length=10, unique=True)),
                ('shorted_url', models.URLField()),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
