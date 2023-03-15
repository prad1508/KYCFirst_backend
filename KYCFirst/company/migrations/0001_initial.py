# Generated by Django 4.1.6 on 2023-03-06 07:45

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=90, unique=True)),
                ('gst_no', models.CharField(max_length=50)),
                ('emailID', models.EmailField(max_length=254)),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Address', models.TextField()),
                ('country', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
                ('pincode', models.IntegerField()),
                ('logo', models.ImageField(upload_to='company_logo')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=80)),
                ('Address', models.TextField()),
                ('emailID', models.EmailField(max_length=254)),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='company.company')),
            ],
        ),
    ]
