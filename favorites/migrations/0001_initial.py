# Generated by Django 3.1.7 on 2021-04-16 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('discussion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoritesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discussion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discussion.discussionmodel')),
            ],
        ),
    ]
