# Generated by Django 5.1.3 on 2024-12-14 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_rename_pubished_date_post_published_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 12, 14, 6, 58, 59, 130567, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
