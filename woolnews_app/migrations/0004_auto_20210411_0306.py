# Generated by Django 3.1.6 on 2021-04-11 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woolnews_app', '0003_merge_20210410_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]