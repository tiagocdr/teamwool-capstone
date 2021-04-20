# Generated by Django 3.1.7 on 2021-04-20 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('favorites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
                ('timestamp', models.TimeField(default=django.utils.timezone.now)),
                ('votes', models.IntegerField(blank=True, default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(max_length=1000)),
                ('img', models.ImageField(blank=True, upload_to='images/')),
                ('timestamp', models.TimeField(default=django.utils.timezone.now)),
                ('genre', models.CharField(choices=[('AT', 'Automotive'), ('SP', 'Sports'), ('AR', 'Arts'), ('PL', 'Politics'), ('CC', 'Climate Change'), ('OP', 'Opinion'), ('DJ', 'DadJokes'), ('GEN', 'General')], default='GEN', max_length=3)),
                ('comments', models.ManyToManyField(blank=True, null=True, to='woolnews_app.CommentModel')),
                ('discussion', models.ManyToManyField(blank=True, null=True, to='discussion.DiscussionModel')),
                ('favs', models.ManyToManyField(blank=True, to='favorites.FavoritesModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
