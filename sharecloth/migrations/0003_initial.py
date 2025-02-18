# Generated by Django 4.0.3 on 2024-05-07 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharecloth', '0002_delete_justtesttable_delete_testtabletwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_num', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('can_land', models.BooleanField()),
                ('price', models.IntegerField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('publisher_name', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.IntegerField()),
                ('user_location', models.DecimalField(decimal_places=5, max_digits=10)),
                ('land_item_info', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
