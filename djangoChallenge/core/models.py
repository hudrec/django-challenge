from django.db import models


class Person(models.Model):
    ROLES = [
        ('AC', 'ACTOR'),
        ('DI', 'DIRECTOR'),
        ('PR', 'PRODUCER'),
    ]
    last_name = models.CharField(
        max_length=255
    )
    first_name = models.CharField(
        max_length=255
    )
    aliases = models.CharField(
        max_length=127
    )
    role = models.CharField(
        max_length=2,
        choices=ROLES
    )


class Movie(models.Model):
    title = models.CharField(
        max_length=255
    )
    release_year = models.IntegerField()
    casting = models.ManyToManyField(
        Person,
        related_name='movies_as_actor'
    )
    directors = models.ManyToManyField(
        Person,
        related_name='movies_as_director'
    )
    producers = models.ManyToManyField(
        Person,
        related_name='movies_as_producer'
    )

