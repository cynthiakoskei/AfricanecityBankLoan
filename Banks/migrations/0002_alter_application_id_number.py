# Generated by Django 4.1.7 on 2023-03-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Banks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="id_number",
            field=models.IntegerField(),
        ),
    ]