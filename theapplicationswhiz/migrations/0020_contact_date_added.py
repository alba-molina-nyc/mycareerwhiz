# Generated by Django 3.2.9 on 2021-12-05 19:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theapplicationswhiz', '0019_alter_contact_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
