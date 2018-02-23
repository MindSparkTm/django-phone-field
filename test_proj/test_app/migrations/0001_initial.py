# Generated by Django 2.0.2 on 2018-02-23 20:36

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phone_field.models.PhoneField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='TestModelOptional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
            ],
        ),
    ]
