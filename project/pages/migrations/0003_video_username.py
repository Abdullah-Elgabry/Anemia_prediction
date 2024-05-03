# Generated by Django 4.1.3 on 2022-11-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_product_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, null=True)),
                ("Product", models.ManyToManyField(null=True, to="pages.video")),
            ],
        ),
    ]
