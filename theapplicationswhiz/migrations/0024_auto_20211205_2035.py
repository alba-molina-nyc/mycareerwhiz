# Generated by Django 3.2.9 on 2021-12-05 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapplicationswhiz', '0023_contact_linkedin_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='application',
            name='category',
        ),
    ]