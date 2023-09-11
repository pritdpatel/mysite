# Generated by Django 4.2.4 on 2023-08-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('productName', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
    ]