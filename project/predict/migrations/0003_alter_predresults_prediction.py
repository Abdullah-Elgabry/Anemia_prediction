# Generated by Django 4.1.3 on 2022-12-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0002_rename_petal_length_predresults_gender_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predresults",
            name="prediction",
            field=models.CharField(max_length=30),
        ),
    ]