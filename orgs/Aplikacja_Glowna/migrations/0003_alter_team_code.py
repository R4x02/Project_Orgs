# Generated by Django 5.1.2 on 2024-11-17 16:19

import Aplikacja_Glowna.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplikacja_Glowna', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='code',
            field=models.CharField(default=Aplikacja_Glowna.models.generate_team_code, max_length=10, unique=True),
        ),
    ]