# Generated by Django 4.1 on 2022-09-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.ImageField(default=0, upload_to='', verbose_name='Количество просмотров'),
        ),
    ]