from django import forms
from .models import Kid_reg

class kidregform(forms.ModelForm):
    objects = None

    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        widget=forms.RadioSelect 
     )

    ALLERGY_CHOICES = [
        ('none', 'None'),
        ('peanuts', 'Peanuts'),
        ('shellfish', 'Shellfish'),
        ('dairy', 'Dairy'),
        ('eggs', 'Eggs'),
        ('gluten', 'Gluten'),
        ('soy', 'Soy'),
        ('tree_nuts', 'Tree Nuts'),
        ('wheat', 'Wheat'),
        ('fish', 'Fish'),
        ('other', 'Other'),
    ]

    allergy = forms.MultipleChoiceField(
        choices=ALLERGY_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    MEDICAL_CONDITIONS_CHOICES = [
        ('none', 'None'),
        ('asthma', 'Asthma'),
        ('diabetes', 'Diabetes'),
        ('heart_disease', 'Heart Disease'),
        ('cancer', 'Cancer'),
        ('high_blood_pressure', 'High Blood Pressure'),
        ('other', 'Other'),
    ]

    medical_conditions = forms.MultipleChoiceField(
        choices=MEDICAL_CONDITIONS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Medical Conditions",
        required=False
    )

    FAMILY_MEDICAL_HISTORY_CHOICES = [
        ('none', 'None'),
        ('asthma', 'Asthma'),
        ('diabetes', 'Diabetes'),
        ('heart_disease', 'Heart Disease'),
        ('cancer', 'Cancer'),
        ('high_blood_pressure', 'High Blood Pressure'),
        ('other', 'Other'),
    ]

    family_medical_history = forms.MultipleChoiceField(
        choices=FAMILY_MEDICAL_HISTORY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Family Medical History",
        required=False
    )

    IDENTIFICATION_CHOICES = [
        ('passport', 'Passport'),
        ('driver_license', 'Driver License'),
        ('state_id', 'State ID'),
        ('birth_certificate', 'Birth Certificate'),
        ('other', 'Other'),
    ]

    guardian_identification_type =forms.ChoiceField(
        choices=IDENTIFICATION_CHOICES,
        # widget=forms.CheckboxSelectMultiple,
        label = "Guardian Identification Type",
    )

    class Meta:
        model = Kid_reg
        fields = "__all__"  # This includes all fields in the model
        labels = {
            'gov_fname': 'Government First Name',
            'gov_lname': 'Government Last Name',
            'date_of_birth': 'Date of Birth',
            'sex': 'Sex',
            'street_address': 'Street Address',
            'city': 'City',
            'state': 'State',
            'zip_code': 'Zip Code',
            'country': 'Country',
            'emergency_contact_fullname': 'Emergency Contact Full Name',
            'emergency_contact_email_address': 'Emergency Contact Email Address',
            'emergency_contact_phone_number': 'Emergency Contact Phone Number',
            'insurance_provider': 'Insurance Provider',
            'insurance_policy_number': 'Insurance Policy Number',
            'group_number': 'Group Number',
            'primary_care_doctor': 'Primary Care Doctor',
            'doctor_phone_number': 'Doctor Phone Number',
            'doctor_hospital_address': 'Doctor Hospital Address',
            'current_medication': 'Current Medication',
            'allergy': 'Allergies',
            'medical_conditions': 'Medical Conditions',
            'family_medical_history': 'Family Medical History',
            'guardian_identification_type': 'Guardian Identification Type',
            'guardian_identification_document': 'Identification Document',
        }