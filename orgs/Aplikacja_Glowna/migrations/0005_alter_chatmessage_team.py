# Generated by Django 5.1.3 on 2024-12-01 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplikacja_Glowna', '0004_chatmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='Aplikacja_Glowna.team'),
        ),
    ]