# Generated by Django 3.2.6 on 2021-08-02 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrderAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='adress',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='OrderAPI.adress'),
        ),
    ]
