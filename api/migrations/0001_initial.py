# Generated by Django 5.0.4 on 2024-04-29 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("department_name", models.CharField(max_length=250)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Student_Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=100)),
                ("reg_number", models.IntegerField(unique=True)),
                ("email", models.EmailField(max_length=254)),
                (
                    "depart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.department"
                    ),
                ),
            ],
        ),
    ]