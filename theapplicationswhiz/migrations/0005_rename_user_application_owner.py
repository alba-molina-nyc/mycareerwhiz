# Generated by Django 3.2.9 on 2021-12-02 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapplicationswhiz', '0004_auto_20211202_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='user',
            new_name='owner',
        ),
    ]
