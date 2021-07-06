from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Engine(models.Model):
    name = models.CharField(max_length=20)
    programming_language = models.CharField(max_length=30)
    release_date = models.DateField(null=True, blank=True)
    developer = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=30)
    management = models.CharField(max_length=18, null=True, blank=True)
    date_of_establishment = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    year_revenue_in_mrd = models.FloatField(null=True, blank=True)
    developer = models.ManyToManyField(Developer)

    def __str__(self):
        return self.name

class Plattform(models.Model):
    name = models.CharField(max_length=18)
    specs = models.TextField()
    description = models.TextField(null=True, blank=True)
    portable = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


usk_choices = (
    ('0', "0"),
    ('6', "6"),
    ('12', "12"),
    ('16', "16"),
    ('18', "18"),
)

class Game(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField(null=True, blank=True)

    cover = models.ImageField(null=True, blank=True, upload_to="templates/static/images")

    description = models.TextField(null=True, blank=True)
    hardware_requirements = models.TextField(null=True, blank=True)
    rating = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])

    plattform = models.ManyToManyField(Plattform)

    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)

    multiplayer = models.BooleanField(default=False)
    crossplay = models.BooleanField(default=False)

    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    developer = models.ManyToManyField(Developer)

    usk = models.CharField(max_length=2, choices=usk_choices, default='0')
    sales = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
