# Generated by Django 5.0.6 on 2024-10-25 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journi', '0002_remove_kid_reg_dietary_restrictions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid_reg',
            name='group_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]