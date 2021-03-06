# Generated by Django 3.2.9 on 2021-12-03 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theapplicationswhiz', '0014_application_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='theapplicationswhiz.application')),
            ],
        ),
    ]
