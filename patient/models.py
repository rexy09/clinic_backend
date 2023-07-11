from django.db import models

# Create your models here.


class Patient(models.Model):
    GENDER = [
        ('male', 'male'),
        ('female', 'female'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        pass


class Visit(models.Model):
    HEALTH = [
        ('good', 'good'),
        ('poor', 'poor'),
    ]
    RADIO = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    patient = models.ForeignKey(
        Patient, related_name='visits', on_delete=models.CASCADE)
    date = models.DateField()
    height = models.DecimalField(max_digits=5, decimal_places=1)
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    bmi = models.DecimalField(max_digits=5, decimal_places=1)
    health = models.CharField(max_length=10, choices=HEALTH)
    on_diet = models.CharField(
        max_length=10,  null=True, choices=RADIO)
    taking_drugs = models.CharField(
        max_length=10,  null=True, choices=RADIO)
    comment = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'

    def __str__(self):
        pass
