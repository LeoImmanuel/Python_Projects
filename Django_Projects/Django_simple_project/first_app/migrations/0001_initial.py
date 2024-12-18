# Generated by Django 4.1 on 2024-10-18 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Topic_class",
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
                ("topic_name", models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Web_page_class",
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
                ("webpage_name", models.CharField(max_length=264, unique=True)),
                ("webpage_url", models.URLField(unique=True)),
                (
                    "webpage_topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="first_app.topic_class",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Web_Access_Record",
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
                ("Web_page_class_date", models.DateField()),
                (
                    "Web_Access_Record_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="first_app.web_page_class",
                    ),
                ),
            ],
        ),
    ]
