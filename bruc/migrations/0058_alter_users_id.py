# Generated by Django 4.0.4 on 2024-02-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bruc', '0057_alter_users_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
