# Generated by Django 5.1.6 on 2025-04-21 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_feed', '0008_news_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='view_count',
        ),
    ]
