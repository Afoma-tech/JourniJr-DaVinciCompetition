from django.db import models
from django_countries.fields import CountryField

class Kid_reg(models.Model):
    # personal information
    gov_fname = models.CharField(max_length=255, default='Unknown', blank=False, null=False)
    gov_lname = models.CharField(max_length=255, default='Unknown', blank=False, null=False)
    guardian_email_address = models.EmailField(default='Unknown',blank=False, null=False)
    guardian_phone_number = models.CharField(max_length=12, null=True)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=255, blank=False, null=True)
    street_address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=20, null=True)
    country = CountryField(default='CA')
    emergency_contact_fullname = models.CharField(max_length=255, default='Unknown', blank=True, null=True)
    emergency_contact_phone_number = models.CharField(max_length=12, null=True)
    # insurance information
    insurance_provider = models.CharField(max_length=255, default='Unknown', blank=True, null=True)
    insurance_policy_number = models.CharField(max_length=13, null=True)
    group_number = models.CharField(max_length=10, null=True)
    # medical information
    primary_care_doctor = models.CharField(max_length=255, default='Unknown', blank=True, null=True)
    doctor_phone_number = models.CharField(max_length=12, null=True)
    current_medication = models.CharField(max_length=12, null=True)
    allergy = models.CharField(max_length=255, default='none')
    medical_conditions = models.CharField(max_length=255, default='none')
    family_medical_history = models.CharField(max_length=255, default='none')
    # identification
    guardian_identification_type = models.CharField(max_length=255, default="Passport")
    child_identification_type = models.CharField(max_length=255, default="Passport")
    guardian_identification_document = models.ImageField(upload_to='mediafile/', null=True)
    child_identification_document = models.ImageField(upload_to='mediafile/', null=True)
    

