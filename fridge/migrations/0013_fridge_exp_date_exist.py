# Generated by Django 4.2.4 on 2023-09-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fridge", "0012_alter_fridge_exp_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="fridge",
            name="exp_date_exist",
            field=models.BooleanField(default=True),
        ),
    ]