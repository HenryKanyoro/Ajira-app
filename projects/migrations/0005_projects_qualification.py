# Generated by Django 3.1.5 on 2021-02-05 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20210204_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='qualification',
            field=models.TextField(default=9, max_length=300),
            preserve_default=False,
        ),
    ]
