# Generated by Django 5.0.6 on 2024-10-26 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journi', '0005_kid_reg_doctor_hospital_address_alter_kid_reg_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kid_reg',
            name='child_identification_document',
        ),
        migrations.RemoveField(
            model_name='kid_reg',
            name='child_identification_type',
        ),
        migrations.AlterField(
            model_name='kid_reg',
            name='allergy',
            field=models.CharField(blank=True, default='none', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='kid_reg',
            name='family_medical_history',
            field=models.CharField(blank=True, default='none', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='kid_reg',
            name='guardian_identification_document',
            field=models.ImageField(blank=True, null=True, upload_to='mediafile/'),
        ),
        migrations.AlterField(
            model_name='kid_reg',
            name='guardian_identification_type',
            field=models.CharField(blank=True, default='Passport', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='kid_reg',
            name='medical_conditions',
            field=models.CharField(blank=True, default='none', max_length=255, null=True),
        ),
    ]
