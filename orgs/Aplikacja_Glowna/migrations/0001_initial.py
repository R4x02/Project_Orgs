# Generated by Django 5.1.2 on 2024-11-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uzytkownik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imie', models.CharField(max_length=100)),
                ('Nazwisko', models.CharField(max_length=100)),
                ('gmail', models.CharField(max_length=100)),
            ],
        ),
    ]
