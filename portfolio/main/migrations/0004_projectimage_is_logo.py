# Generated by Django 5.0.6 on 2024-07-07 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='is_logo',
            field=models.BooleanField(default=False),
        ),
    ]
