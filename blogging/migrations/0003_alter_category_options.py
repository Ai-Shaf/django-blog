# Generated by Django 3.2 on 2023-05-22 05:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogging", "0002_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]
