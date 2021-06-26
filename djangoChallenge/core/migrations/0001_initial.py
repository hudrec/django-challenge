# Generated by Django 3.2.4 on 2021-06-24 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('aliases', models.CharField(max_length=127)),
                ('role', models.CharField(choices=[('AC', 'ACTOR'), ('DI', 'DIRECTOR'), ('PR', 'PRODUCER')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('casting', models.ManyToManyField(related_name='movies_as_actor', to='core.Person')),
                ('directors', models.ManyToManyField(related_name='movies_as_director', to='core.Person')),
                ('producers', models.ManyToManyField(related_name='movies_as_producer', to='core.Person')),
            ],
        ),
    ]