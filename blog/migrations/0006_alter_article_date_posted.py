# Generated by Django 3.2.8 on 2021-10-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20211015_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_posted',
            field=models.DateTimeField(default='2021-10-15 10:19:24'),
        ),
    ]
