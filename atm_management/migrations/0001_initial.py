# Generated by Django 4.2.5 on 2024-04-13 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm_management.state')),
            ],
        ),
        migrations.CreateModel(
            name='ATMSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('site_id', models.CharField(max_length=50, unique=True)),
                ('address', models.TextField()),
                ('contact_details', models.JSONField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm_management.city')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm_management.state')),
            ],
        ),
    ]
