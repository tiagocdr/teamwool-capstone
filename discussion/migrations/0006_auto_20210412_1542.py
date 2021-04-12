# Generated by Django 3.1.7 on 2021-04-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woolnews_app', '0005_merge_20210411_0339'),
        ('discussion', '0005_auto_20210412_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussionmodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='discussionmodel',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='woolnews_app.CommentModel'),
        ),
    ]