# Generated by Django 5.1.1 on 2024-12-28 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=50)),
            ],
        ),
    ]
