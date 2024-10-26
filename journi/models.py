from django.db import models
from django_countries.fields import CountryField

class Kid_reg(models.Model):
    # personal information
    gov_fname = models.CharField(max_length=255, default='Unknown', blank=True, null=False)
    gov_lname = models.CharField(max_length=255, default='Unknown', blank=True, null=False)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=255, blank=True, null=True)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(default='CA')
    emergency_contact_fullname = models.CharField(max_length=255, default='Unknown', blank=True, null=True)
    emergency_contact_email_address = models.CharField(max_length=255,blank=True, null=False)
    emergency_contact_phone_number = models.CharField(max_length=12, null=True, blank=True)
    # insurance information
    insurance_provider = models.CharField(max_length=255, default='Unknown', blank=True, null=True)
    insurance_policy_number = models.CharField(max_length=13, blank=True, null=True)
    group_number = models.CharField(max_length=10, blank=True, null=True)
    # medical information
    primary_care_doctor = models.CharField(max_length=255, default='Unknown', blank=True, null=True)
    doctor_phone_number = models.CharField(max_length=12, null=True, blank=True)
    doctor_hospital_address = models.CharField(max_length=255, default='Unknown', blank=True, null=True)
    current_medication = models.CharField(max_length=12, null=True, blank=True)
    allergy = models.CharField(max_length=255, default='none', null=True, blank=True)
    medical_conditions = models.CharField(max_length=255, default='none', null=True, blank=True)
    family_medical_history = models.CharField(max_length=255, default='none', null=True, blank=True)
    # identification
    guardian_identification_type = models.CharField(max_length=255, default="Passport", null=True, blank=True)
    guardian_identification_document = models.ImageField(upload_to='mediafile/', null=True, blank=True)
    
    def __str__(self):
        return self.gov_fname
    

