from django.db import models
from django.core.exceptions import ValidationError
import datetime

def date_validator(date):
    if date > datetime.date.today():
        raise ValidationError('Date greater than Today!')

# Create your models here.

class Squirrel(models.Model):
    """
    Squirrel
    """
    latitude = models.DecimalField(max_digits=30, decimal_places=25)
    longitude = models.DecimalField(max_digits=30, decimal_places=25)
    unique_squirrel_id = models.CharField(max_length=32, primary_key=True)
    SHIFT_CHOICES = (
        ('AM', 'AM'),
        ('PM', 'PM'),
    )
    shift = models.CharField(max_length=2, choices=SHIFT_CHOICES)
    date = models.DateField(verbose_name='date', validators=[date_validator])
    AGE_CHOICES = (
        ('Adult', 'Adult'),
        ('Juvenile', 'Juvenile'),
    )
    age = models.CharField(verbose_name='age', max_length=10, choices=AGE_CHOICES, null=True, blank=True)
    PRIMARY_FUR_COLOR_CHOICES = (
        ('Gary', 'Gray'),
        ('Cinnamon', 'Cinnamon'),
        ('Blank', 'Black'),
    )
    primary_fur_color = models.CharField(max_length=20, choices=PRIMARY_FUR_COLOR_CHOICES, null=True, blank=True)
    LOCATION_CHOICES = (
        ('Ground Plane', 'Ground Plane'),
        ('Above Ground', 'Above Ground'),
    )
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, blank=True, null=True)
    specific_location = models.CharField(max_length=255, blank=True, null=True)
    running = models.BooleanField(default=False)
    chasing = models.BooleanField(default=False)
    climbing = models.BooleanField(default=False)
    eating = models.BooleanField(default=False)
    foraging = models.BooleanField(default=False)
    other_activities = models.TextField(blank=True, null=True, verbose_name='Other Activities')
    kuks = models.BooleanField(default=False)
    quaas = models.BooleanField(default=False)
    moans = models.BooleanField(default=False)
    tail_flags = models.BooleanField(default=False)
    tail_twitches = models.BooleanField(default=False)
    approaches = models.BooleanField(default=False)
    indifferent = models.BooleanField(default=False)
    runs_from = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = "Squirrel"
        verbose_name_plural = verbose_name
        ordering = ('-date',)

    def __str__(self):
        return self.unique_squirrel_id
