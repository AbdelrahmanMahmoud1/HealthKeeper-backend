# Generated by Django 5.0.3 on 2024-04-11 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='EmergencyMobileNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobileNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]