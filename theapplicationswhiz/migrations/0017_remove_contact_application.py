# Generated by Django 3.2.9 on 2021-12-03 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapplicationswhiz', '0016_contact_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='application',
        ),
    ]
