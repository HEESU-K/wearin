# Generated by Django 5.0.5 on 2024-06-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sharecloth", "0012_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tpo",
            field=models.CharField(
                blank=True,
                choices=[
                    ("campus", "CAMPUS"),
                    ("date", "DATE"),
                    ("wedding", "WEDDING"),
                    ("daily", "DAILY"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
