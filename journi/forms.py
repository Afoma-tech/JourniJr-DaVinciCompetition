from django import forms
from .models import Kid_reg

class kidregform(forms.ModelForm):
    objects = None

    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    sex = forms.RadioSelect(
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

    FAMILY_MEDICAL_HISTORY_CHOICES = [
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

    CHILD_IDENTIFICATION_CHOICES = [
        ('birth_certificate', 'Birth Certificate'),
        ('passport', 'Passport'),
        ('other', 'Other'),
    ]

    child_identification_type = forms.ChoiceField(
        choices=CHILD_IDENTIFICATION_CHOICES,
        # widget=forms.CheckboxSelectMultiple,
        label= "Child Identification Type",
    )

    class Meta:
        model = Kid_reg
        fields = "__all__"  # This includes all fields in the model
        labels = {
            'gov_fname': 'Government First Name',
            'gov_lname': 'Government Last Name',
            'guardian_email_address': 'Guardian Email Address',
            'guardian_phone_number': 'Guardian Phone Number',
            'date_of_birth': 'Date of Birth',
            'sex': 'Sex',
            'street_address': 'Street Address',
            'city': 'City',
            'state': 'State',
            'zip_code': 'Zip Code',
            'country': 'Country',
            'emergency_contact_fullname': 'Emergency Contact Full Name',
            'emergency_contact_phone_number': 'Emergency Contact Phone Number',
            'insurance_provider': 'Insurance Provider',
            'insurance_policy_number': 'Insurance Policy Number',
            'primary_care_doctor': 'Primary Care Doctor',
            'doctor_phone_number': 'Doctor Phone Number',
            'current_medication': 'Current Medication',
            'allergy': 'Allergies',
            'medical_conditions': 'Medical Conditions',
            'family_medical_history': 'Family Medical History',
            'guardian_identification_type': 'Guardian Identification Type',
            'chid_identification_type': 'Child Identification Type',
            'identification_document': 'Identification Document',
        }