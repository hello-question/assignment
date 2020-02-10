from datetime import date

from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models
from django.urls import reverse


# Create your models here.
alphabets = RegexValidator(r'^[a-zA-Z](?!.*\s{2}).*[a-zA-Z]$',
                              'Only alphabets are allowed.')


class Housing(models.Model):
    LANDED = 'Landed'
    CONDOMINIUM = 'Condominium'
    HDB = 'HDB'
    HOUSEHOLD_TYPE = (
        (LANDED, 'Landed'),
        (CONDOMINIUM, 'Condominium'),
        (HDB, 'HDB'),
    )
    housing_type = models.CharField(max_length=11,
                                    choices=HOUSEHOLD_TYPE,
                                    default=HDB)

    def __str__(self):
        return self.housing_type


class Household(models.Model):
    housing_type_id = models.ForeignKey(Housing, on_delete=models.CASCADE)
    household_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.household_name

    def get_absolute_url(self):
        # return reverse("grants:household-list")
        return reverse("grants:household-detail", kwargs={"id": self.id})


class Gender(models.Model):
    FEMALE = 'Female'
    MALE = 'Male'
    GENDER = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )

    gender = models.CharField(max_length=6,
                              choices=GENDER,
                              default=FEMALE)

    def __str__(self):
        return self.gender


class MaritalStatus(models.Model):
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    SEPARATED = 'Separated'
    WIDOWED = 'Widowed'
    MARTIAL_STATUS = (
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (DIVORCED, 'Divorced'),
        (SEPARATED, 'Separated'),
        (WIDOWED, 'Widowed'),
    )

    marital_status = models.CharField(max_length=9,
                                      choices=MARTIAL_STATUS,
                                      default=SINGLE)

    def __str__(self):
        return self.marital_status


class OccupationType(models.Model):
    EMPLOYED = 'Employed'
    UNEMPLOYED = 'Unemployed'
    STUDENT = 'Student'
    OCCUPATION_TYPE = (
        (EMPLOYED, 'Employed'),
        (UNEMPLOYED, 'Unemployed'),
        (STUDENT, 'Student'),
    )

    occupation_type = models.CharField(max_length=10,
                                       choices=OCCUPATION_TYPE,
                                       default=EMPLOYED)

    def __str__(self):
        return self.occupation_type


class FamilyMember(models.Model):
    household_type_id = models.ForeignKey(Household, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, validators=[alphabets],
                            unique=True)
    gender_id = models.ForeignKey(Gender, on_delete=models.CASCADE)
    marital_status_id = models.ForeignKey(MaritalStatus,
                                          on_delete=models.CASCADE)
    spouse = models.CharField(max_length=100,
                              blank=True,
                              null=True)
    occupation_type_id = models.ForeignKey(OccupationType,
                                           on_delete=models.CASCADE)
    annual_income = models.DecimalField(decimal_places=2, max_digits=100)
    date_of_birth = models.DateField(validators=
                                     [MaxValueValidator(
                                         limit_value=date.today
                                     )])

    def get_absolute_url(self):
        return reverse("grants:household-list")

