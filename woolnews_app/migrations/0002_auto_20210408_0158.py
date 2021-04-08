# Generated by Django 3.1.7 on 2021-04-08 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0003_discussionmodel_body'),
        ('woolnews_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='woolnews_app.CommentModel'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='discussion',
            field=models.ManyToManyField(blank=True, null=True, to='discussion.DiscussionModel'),
        ),
    ]
