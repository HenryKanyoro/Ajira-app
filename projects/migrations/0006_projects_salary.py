# Generated by Django 3.1.5 on 2021-02-05 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_projects_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='salary',
            field=models.CharField(default='', max_length=30),
        ),
    ]
