# Generated by Django 4.0.4 on 2022-10-19 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bruc', '0043_rename_amountl_cjenik_volume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cjenik',
            old_name='priceHR',
            new_name='priceHRK',
        ),
    ]
