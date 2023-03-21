# Generated by Django 4.1.7 on 2023-03-21 17:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Loan_Request",
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
                (
                    "Loan_ammount",
                    models.FloatField(
                        default=10000,
                        validators=[
                            django.core.validators.MinValueValidator(10000),
                            django.core.validators.MaxValueValidator(250000),
                        ],
                    ),
                ),
            ],
        ),
    ]