# Generated by Django 3.2.9 on 2021-12-03 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapplicationswhiz', '0012_delete_interviewing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
