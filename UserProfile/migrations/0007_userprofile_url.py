# Generated by Django 5.0.3 on 2024-04-17 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0006_alter_userprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='url',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]