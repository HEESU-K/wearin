# Generated by Django 5.0.5 on 2024-05-23 23:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sharecloth", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="post",
            name="thumbnail",
            field=models.ImageField(upload_to="thumbnails/"),
        ),
    ]
