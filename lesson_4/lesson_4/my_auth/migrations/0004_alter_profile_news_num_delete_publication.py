# Generated by Django 4.0 on 2024-01-20 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0003_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='news_num',
            field=models.IntegerField(default=0, verbose_name='кол-во публикаций'),
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
