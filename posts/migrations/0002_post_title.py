# Generated by Django 4.2.4 on 2023-08-23 05:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="title",
            field=models.CharField(default="title", max_length=50),
        ),
    ]
